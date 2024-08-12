import { useState } from 'react';

import Header from './components/Header.jsx';
import User_input from './components/User_input.jsx';
import Results from './components/Results.jsx';


function App() {
  const [userInput, setUserInput] = useState({
    initialInvestment: null,
    annualInvestment: null,
    expectedReturn: null,
    duration: null
});

function handleChange(inputIdentifier, newValue) {
  setUserInput(prevUserInput => {
      return {...prevUserInput,
      [inputIdentifier]: newValue
      };
  });
}
  
  return (
    <>  
      <Header />
      <User_input onChange={handleChange} userInput={userInput}/>
      <Results userInput={userInput}/>
    </>);
}

export default App
