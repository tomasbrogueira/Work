# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:15:11 2023

@author: tiago
"""

import random
import numpy as np
import csv
import math
from time import sleep
from copy import deepcopy

import json
from matplotlib import pyplot as plt
from scipy.stats import multivariate_normal

#parametros livres
step=0.05 #era 0.05
Gain=3
Gain2=0.75
Qt=0.01 #variancia #era 0.25
Qq=0.0008
 #estava a 0.01
N_PARTICLES = 40
threshold=-1
SAMPLES = 1000
reducefactor=2
skip =30

class Particle():
    def __init__(self, x, y, theta):
        self.pose=[x,y,theta]
        self.start_theta = theta
        self.landmarks=[]
        self.weight = -1
        


def generat_part(firststop, Qq):
    part_list = []   
    for i in range(N_PARTICLES):
        x = np.random.normal(firststop[0], math.sqrt(Qq))
        y = np.random.normal(firststop[1], math.sqrt(Qq))
        theta = np.random.normal(firststop[2], math.sqrt(Qq))
        #print("thet", theta)
        part_list.append(Particle(x, y, theta))
    return part_list
        
def generat_part2(firststop, Qq):
    part_list = []   
    first=random.random()*2*math.pi/N_PARTICLES
    for i in range(N_PARTICLES):
        x = 0
        y = 0
        theta = first + i*2*math.pi/N_PARTICLES
        #print("thet", theta)
        part_list.append(Particle(x, y, theta))
    return part_list

def belongsto(sample, list, step):
    
    maxdiscontinuos=0.6 #era 0.6
    der=(sample[0]-list[-1][0])
    if step > 0.1:
        return False
    
    #der=(sample[0]-list[-1][0])/(sample[1]-list[-1][1])
    if abs(der)<maxdiscontinuos:
        return True
    #print("DER: ", der)
    return False

def separate2(data, step):
    result=[]
    counter=0
    lim=10
    min_obj = 1
    current=[data[0]]
    backup=[]
    i=1
    #plt.figure()
    #print(step)
    while i < len(data):
        step1 = abs(data[i][1]-current[-1][1])
        #print("UM: ", step)
        if belongsto(data[i],current, step1):
            if data[i][0] > 0.1:
                current.append(data[i])
                backup=[]
        else: 
            if len(backup)>0:
                step2 = abs(data[i][1]-backup[-1][1])
                #print("DOIS: ", step)
                if belongsto(data[i],backup,step2):
                    backup.append(data[i])
                elif len(backup) < 3:
                    backup=[data[i]]
            else:
                if data[i][0] > 0.1:
                    backup.append(data[i])
            if len(backup)>lim:
                if len(current) > min_obj:
                    result.append(current)
                #plt.plot(current[0], current[1])
                current=backup
                backup=[]
                
        i=i+1
    if len(current) > min_obj:
        result.append(current)
    #plt.figure()
    #for obj in result:
    #    print("obj",obj[0])
    #    to=np.transpose(obj)
    #    plt.plot(to[1],to[0])
    #plt.show()
    return result

def removebeggining(lidarline):
    #print(lidarline)
    proximity=0.1
    while lidarline[0][0]<proximity:
        lidarline.pop(0)
    return lidarline

def read_dados(filename,reducefactor):
    position = []
    lidar_data = []
    all_lidar_data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        ref = next(csv_reader)
        
        angle_step = float(ref[7])
        j=0
        for row in csv_reader:
            position.append([float(row[1])-float(ref[1]), float(row[2])-float(ref[2]), float(row[3])])
            lidar_data = []
            angle = float(row[5])
            
            for x in json.loads(row[8].replace("nan", "null")):
                angle += float(row[7])
                if j%reducefactor == 0:
                    if x != "null" and x is not None:
                        lidar_data.append([float(x), angle])
                j += 1
            all_lidar_data.append(lidar_data)
                
    return position, all_lidar_data, angle_step


def adaptpart_list(part_list):
    soma=0
    n=0
    for part in part_list:
        #print("w",part.weight)
        if part.weight>-1:
            soma=soma+part.weight
            n=n+1
    if n==0:
        soma=1
        n=1
    for part in part_list:
        if part.weight==-1:
            part.weight=soma/n
    
    soma=0
    for part in part_list:
        soma+=part.weight
    for part in part_list:
        part.weight=part.weight*len(part_list)/soma
        
    return part_list
  

#coisas estranhas aqui se passam          
def stochastic_universal_sampling(part_list):
    randompercentage=0.25
    
    part_list2=adaptpart_list(part_list)
    fitness_values=[p.weight for p in part_list2]
    print(fitness_values)
    
    
    num_selections=len(fitness_values)
    total_fitness = sum(fitness_values)
    
    #num_individuals = len(fitness_values)
    distance = total_fitness / (num_selections*0.75) 

    pointer = random.uniform(0, distance)
    #pointers = [start_point + i * distance for i in range(num_selections)]

    selected_indices = []
    current_sum = fitness_values[0]
    current_index = 0

    while pointer<total_fitness:
        if pointer<current_sum:
            selected_indices.append(current_index)
            pointer+=distance
        else:
            current_index += 1
            current_sum=current_sum+fitness_values[current_index]
        
    #for pointer in pointers:
    #    while current_sum < pointer:
    #        current_index += 1
    #        current_sum += fitness_values[current_index]
    #    selected_indices.append(current_index)
        
    new_particles=[]
    for ind in selected_indices:
        new_particle = deepcopy(part_list2[ind])
        new_particle.weight = 1
        new_particles.append(new_particle)
        
    for i in range(int(len(part_list)*randompercentage)):
        new_particle = deepcopy(part_list2[int(random.random()*len(part_list))])
        new_particle.weight = 1
        new_particles.append(new_particle)
        
    return  new_particles

def getthreebest(part_list):
    first,second,third= 0,0,0
    pos1,pos2,pos3=-1,-1,-1
    for i in range(len(part_list)):
        if part_list[i].weight>first:
            first=part_list[i].weight
            pos1=i
        elif part_list[i].weight>second:
            second=part_list[i].weight
            pos2=i
        elif part_list[i].weight>third:
            third=part_list[i].weight
            pos3=i
    if len(part_list)==1:
        return [part_list[0]]
    if len(part_list)==2:
        return [part_list[pos1],part_list[pos2]]
    print(len(part_list))
    return [part_list[pos1],part_list[pos2], part_list[pos3]]

#this is the stuff
def drawbestguesses(part_list):
    visibility=0.9
    bestparts=getthreebest(part_list)
    for i in range(len(bestparts)):
        plt.figure()
        if i==3:
            continue
        #print(len(bestparts[i].landmarks))
        j=1
        
        transformada=bestparts[i].landmarks
        #color='red'
        plt.title("Best Guess:"+str(bestparts[i].weight))
        transposta=np.transpose(transformada[0])
        if j==1:
            transposta=np.transpose(transformada[0])
            sc= plt.scatter(transposta[0], transposta[1],s=4, c=transformada[1], cmap="Greens")
            plt.colorbar(sc)
        else:
            for i in range(len(transformada[1])):
                if transformada[1][i]>visibility:
                    plt.plot(transformada[0][i][0], transformada[0][i][1],'o')
            print("Not good, not good at all")
        plt.show()
            
def roundtostep(x, step):
    a = round(x/step)
    a = a*step
    return a
    
def transformadagloriatotal(mius, Qt,step):
    points=getpoints(mius, Qt ,step)
    #print("Got points")
    #print(len(points))

    f=[0]*len(points)
    #print("points!",points)
    for miu in mius:
        rv=multivariate_normal(miu,Qt/50)
        for i in range(len(points)):
            point=points[i]
            value=rv.pdf(points[i])
            f[i]=f[i]+value
    #print("f",f)
    transformada=[points,f]
    #drawtransformadavsmius(transformada, mius)
    return transformada

def getclosestindexes(points, mius):
    min_distance = [float('inf')]*len(points)
    result=[-1]*len(points)

    for i, p in enumerate(mius):
        for j,point in enumerate(points):
            distance = math.sqrt((p[0] - point[0])**2 + (p[1] - point[1])**2)
            if distance < min_distance[j]:
                min_distance[j] = distance
                result[j] = i
    return result

def transformadagloriatotal2(mius, Qt, step):
    points=getpoints(mius, Qt ,step)
    idxs=getclosestindexes(points, mius)
    f=[0]*len(points)
    for i, point in enumerate(points):
        rv=multivariate_normal(mius[idxs[i]],Qt)
        f[i] = rv.pdf(points[i])
    transformada=[points,f]
    #drawtransformadavsmius(transformada, mius)
    return transformada

def drawtransformadavsmius(transformada, mius):
    plt.figure();
    plt.title(len(transformada[1]))
    transposta=np.transpose(transformada[0])
    scatter=plt.scatter(transposta[0], transposta[1],s=50, c=transformada[1], cmap="Greens")   
    visualizeMius(mius) 
    #plt.colorbar(scatter)
    plt.show()
   
def barreiraazero(newvalue, statevalue):
    result=newvalue-statevalue
    if result<0:
        return 0
    return result

def cleantransformada(points, f):
    minvalue=8
    i=0
    while i<len(f):
        if f[i]<minvalue:
            f.pop(i)
            points.pop(i)
        else:
            i=i+1
    return [points, f]

def complicatedsum(statevalue, newvalue, Gain2):
    if Gain2==0.5:
        return 0.75*(min(statevalue, newvalue)+max(statevalue, newvalue)/2)
    else:
        return complicatedsum(complicatedsum(statevalue, newvalue, 0.5), statevalue,0.5)

def cleanbulkiness(points, f,step):
    backup=[points, f]
    for i in range(len(points)):
        side1=[backup[0][i][0]+step,backup[0][i][1]]
        side2=[backup[0][i][0]-step,backup[0][i][1]]
        side3=[backup[0][i][0],backup[0][i][1]+step]
        side4=[backup[0][i][0],backup[0][i][1]-step]
        f[i]=(getvalue(backup,side1)+getvalue(backup,side2)+getvalue(backup,side3)+getvalue(backup,side4))/4
    return [points, f]

def cleanbulkiness2(points, f,step):
    backup=[points, f]
    for i in range(len(points)):
        side1=[backup[0][i][0]+step,backup[0][i][1]]
        side2=[backup[0][i][0]-step,backup[0][i][1]]
        side3=[backup[0][i][0],backup[0][i][1]+step]
        side4=[backup[0][i][0],backup[0][i][1]-step]
        f[i]=(getvalue(backup,side1)+getvalue(backup,side2)+getvalue(backup,side3)+getvalue(backup,side4))/4
    return [points, f]

def atualizartransformada(state,new,Gain,step):
    points=getatualizacaopoints(state[0],new[0])
    #print("npoints", len(points))
    f=[0]*len(points)
    difference=0
    inter=0
    counter=0
    for i in range(len(points)):
        statevalue=getvalue(state, points[i])
        newvalue=getvalue(new,points[i])
        if statevalue==0:
            f[i]=newvalue
        elif newvalue==0:
            f[i]=statevalue
        else:
            counter+=1
            f[i]=max(statevalue, newvalue)
            #f[i]=(1-Gain2)*statevalue+Gain2*newvalue
            #f[i]=complicatedsum(statevalue, newvalue, Gain2)
            inter=inter+min(statevalue,newvalue)
            difference=difference+abs(statevalue-newvalue)
    transformada=[points, f]
    #transformada=cleanbulkiness(points, f,step)
    transformada=cleantransformada(transformada[0], transformada[1])
    #print("cleaned", len(transformada[1]))
    #print("diff", difference, len(points))
    if difference==0:
        return [transformada, inter*1000]
    #print("inter", inter, difference)
    return [transformada,inter/difference]

def atualizartransformada2(state,new,Gain,step):
    points=getatualizacaopoints(state[0],new[0])
    #print("npoints", len(points))
    f=[0]*len(points)
    difference=0
    inter=0
    joined=[]
    thisint=0
    stateint=0
    newint=0
    for i in range(len(points)):
        statevalue=getvalue(state, points[i])
        newvalue=getvalue(new,points[i])
        if statevalue==0:
            f[i]=newvalue
        elif newvalue==0:
            f[i]=statevalue
        else:
            joined.append(i)
            #f[i]=statevalue*newvalue
            f[i]=((statevalue**Gain)*newvalue)**(2/(Gain+1))
            thisint+=f[i]
            stateint+=statevalue
            newint+=newvalue
        inter=inter+min(statevalue,newvalue)
        difference=difference+abs(statevalue-newvalue)
    for i in joined:
        print("firstf", f[i])
        f[i]=math.sqrt(f[i]*math.sqrt(newint*stateint)/thisint)
        print("secondf", f[i])
    transformada=cleantransformada(points, f)
    #print("cleaned", len(transformada[1]))
    #print("diff", difference, len(points))
    if difference==0:
        return [transformada, inter*1000]
    return [transformada,inter/difference]

def getvalue(transformada,point):
    #print(transformada)
    for i in range(len(transformada[0])):
        #print(transformada[0][i])
        #if abs(transformada[0][i][0]-point[0])<0.02 and abs(transformada[0][i][1]-point[1])<0.02:
        #    print("miu, trans", point, transformada[0][i])
        if transformada[0][i][0]==point[0] and transformada[0][i][1]==point[1]:
            return transformada[1][i]
    return 0
    
def getpoints(mius, Qt, step):
    points=[]
    sidewidth=3
    n = 4
    for miu in mius:
        #[start,end,num]=getlinspacevalues(miu[0]-n*step,miu[0]+n*step,step)
        start = roundtostep(roundtostep(miu[0], step)-n*step, step)
        end = roundtostep(roundtostep(miu[0], step)+n*step, step)
        num = roundtostep((end-start)/step, 1)
        #print("MIUUUU: ", miu[0], miu[1])
        #print("X LINESPACE: ", np.linspace(start,end,num+1))
        for x in np.linspace(start,end,num+1):
            #[start,end,num]=getlinspacevalues(miu[1]-n*step,miu[1]+n*step,step)
            start1 = roundtostep(roundtostep(miu[1], step)-n*step, step)
            end1 = roundtostep(roundtostep(miu[1], step)+n*step, step)
            num1 = roundtostep((end1-start1)/step, 1)
            #print("START: ", start1, "END: ", end1, "NUM: ", num1)
            #print("Y LINESPACE: ", np.linspace(start1,end1,num1+1))
            for y in np.linspace(start1,end1,num1+1):
                points.append([roundtostep(x, step),roundtostep(y,step)]) 
                #print("POINT APPENDED: ",[roundtostep(x, step),roundtostep(y,step)])
    #print("points pre oder", points)            
    result=orderandcut(points)
    #print("points pos order", result)            
    return result

def getatualizacaopoints(old, new):
    return orderandcut(old+new)    

def orderandcut(points):
    result=np.unique(points,axis=0).tolist()
    return result

def closecost(miu, point, value):
    return (((miu[0]-point[0])**2)+((miu[1]-point[1])**2))/math.sqrt(value)

def getclosest(miufirst, miulast, transformada):
    end1=transformada[0][0]
    end2=transformada[0][0]
    min1=closecost(miufirst, end1,transformada[1][0])
    min2=closecost(miulast, end1,transformada[1][0])
    for i in range(len(transformada[1])):
        if closecost(miufirst, transformada[0][i], transformada[1][i])<min1:
            min1=closecost(miufirst, transformada[0][i], transformada[1][i])
            end1=transformada[0][i]
        if closecost(miulast, transformada[0][i], transformada[1][i])<min2:
            min2=closecost(miulast, transformada[0][i], transformada[1][i])
            end2=transformada[0][i]
    return [end1, end2]

def linecost(miufirst, miulast, end1, end2):
    deltatheta=abs(math.atan2(miufirst[1]-miulast[1],miufirst[0]-miulast[0])-math.atan2(end1[1]-end2[1],end1[0]-end2[0]))
    dist1=math.sqrt(((miufirst[0]-end1[0])**2)+((miufirst[1]-end1[1])**2))
    dist2=math.sqrt(((miulast[0]-end2[0])**2)+((miulast[1]-end2[1])**2))
    #print("first and cost", miufirst, end1, dist1, dist2, deltatheta)
    return dist1*dist2*deltatheta
    

def findlandmark(xt, first, last, landmarks):
    limite=100
    pos=-1
    miufirst=[xt[0]+first[0], xt[1]+first[1]]
    miulast=[xt[0]+last[0], xt[1]+last[1]]
    mincost=10000
    for i in range(len(landmarks)):
        landmark=landmarks[i]
        #plt.figure()
        #transposta=np.transpose(landmark[0])
        #sc= plt.scatter(transposta[0], transposta[1],s=200, c=landmark[1], cmap="Greens")
        #plt.plot([miufirst[0],miulast[0]],[miufirst[1],miulast[1]],'o')
        #plt.show()
        [end1, end2]=getclosest(miufirst, miulast, landmark)
        
        if linecost(miufirst, miulast, end1, end2)<mincost:
            mincost=linecost(miufirst, miulast, end1, end2)
            pos=i
    if mincost>limite:
        pos=-1
    #print("min", mincost)
    #print("answer to all problems", pos)
    return pos

def hmenosum(zk, xt):
    return (zk[0]+xt[0], zk[1]+xt[1])

def updateweight(weight, difference):
    if weight==-1:
        return difference
    return weight*difference

def getends(zu, pose):
    first=zu[0]
    last=zu[-1]
    firstcor=[first[0]*math.cos(first[1]),first[0]*math.sin(first[1])]
    firstfinal=np.dot(firstcor, [[math.cos(pose[2]), -math.sin(pose[2])], [math.sin(pose[2]), math.cos(pose[2])]])
    lastcor=[last[0]*math.cos(last[1]),last[0]*math.sin(last[1])]
    lastfinal=np.dot(lastcor, [[math.cos(pose[2]), -math.sin(pose[2])], [math.sin(pose[2]), math.cos(pose[2])]])
    return [firstfinal, lastfinal]

def getmatch(zu, pose, landmarks):
    [first, last]=getends(zu, pose)
    pos = findlandmark(pose, first, last, landmarks)
    return pos

def updatepose(particle, pathi, pathmenos, Qq):
    newx=particle.pose[0]+np.random.normal(pathi[0]-pathmenos[0],math.sqrt(Qq))
    newy=particle.pose[1]+np.random.normal(pathi[1]-pathmenos[1],math.sqrt(Qq))
    newtheta=particle.pose[2]+np.random.normal(pathi[2]-pathmenos[2],math.sqrt(Qq))
    particle.pose=(newx,newy,newtheta)
    return particle

def weightcalculation(particle, zx, threshold, Qt, Qq):
    mius=[]
    for ze in zx:
        #For each measurement calculate position
        newdir=[ze[0]*math.cos(ze[1]+particle.pose[2]), ze[0]*math.sin(ze[1]+particle.pose[2])]
        #zint=[ze[0]*math.cos(ze[1]),ze[0]*math.sin(ze[1])]
        #zj=np.dot(zint, [[math.cos(particle.pose[2]), -math.sin(particle.pose[2])], [math.sin(particle.pose[2]), math.cos(particle.pose[2])]])
        mius.append(hmenosum(newdir, particle.pose)) 
    gloriaatual=transformadagloriatotal2(mius,Qt,step)
    #print(mius)
    #visualizeMius(mius)
    if i==0:
        #inicializacao
        particle.landmarks=gloriaatual
    else:
        [transformada,difference]=atualizartransformada(particle.landmarks,gloriaatual, Gain, step)
        particle.landmarks=transformada
        particle.weight=updateweight(particle.weight, difference)
    return particle
            
def visualizeMius(mius):
    x, y = zip(*mius)
    plt.scatter(x, y)
    plt.show()


def plotdirect(path, skip, lidar_data):
    plt.figure()  
    for i in range(len(path)//skip-1):
        
        for element in lidar_data[i*skip]:
            zint=[element[0]*math.cos(element[1]),element[0]*math.sin(element[1])]
            zj=np.dot(zint, [[math.cos(path[i*skip][2]), -math.sin(path[i*skip][2])], [math.sin(path[i*skip][2]), math.cos(path[i*skip][2])]])
            newdir=[element[0]*math.cos(element[1]+path[i*skip][2]), element[0]*math.sin(element[1]+path[i*skip][2])]
            plt.plot(newdir[0]+path[i*skip][0],newdir[1]+path[i*skip][1],'o')
        
        if i==40:
            break
    plt.show()
    
def drawallparticles(bestparts):
    visibility=12
    j=1
    for i in range(len(bestparts)):
         plt.figure()
         #print(len(bestparts[i].landmarks))
         print("n objects ", len(bestparts[i].landmarks))
         transformada=bestparts[i].landmarks
         #color='red'
         plt.title("Best Guess:"+str(bestparts[i].weight))
         if j==1:
             transposta=np.transpose(transformada[0])
             sc= plt.scatter(transposta[0], transposta[1],s=4, c=transformada[1], cmap="Greens")
             plt.colorbar(sc)
         else:
             for i in range(len(transformada[1])):
                 if transformada[1][i]>visibility:
                     plt.plot(transformada[0][i][0], transformada[0][i][1],'o')
         plt.show() 
    
start=[0,0]

filename = 'dados_tratados.csv'
path, lidar_data, angle_step=read_dados(filename, reducefactor)

#measureddistances=generatedistancesdata(path, mapa, samples, measurenoise)
part_list = generat_part(path[0], Qq)

    
plotdirect(path, skip, lidar_data)

for i in range(len(path)//skip-1):
    print("ola?", i)
    #plt.figure()
    #pos=path[i*skip]
    #if i<10:
    #    continue
    #zt = separate2(lidar_data[i*skip], angle_step)
    for j in range(len(part_list)):
       # plt.figure()
        part_list[j]=weightcalculation(part_list[j], removebeggining(lidar_data[i*skip]), threshold,Qt,Qq)
        #plt.plot(part_list[j].pose[0],part_list[j].pose[1],'o')
        #plt.show()
        part_list[j]=updatepose(part_list[j],path[(i+1)*skip], path[i*skip], Qq)
    part_list = stochastic_universal_sampling(part_list)
    #print("Values",part_list[0].landmarks[1])
    if i%4==0:
        drawbestguesses(part_list)
    print("ITERACAO: ", i*skip)


drawallparticles(part_list)

#for i in range(len(path)//skip-1):
#    break
#    print(path[i*skip])