import { calculateInvestmentResults, formatter } from "../util/investment";


export default function Results({ userInput }) {
    const results = calculateInvestmentResults(userInput);
    
    if (!results || results.length === 0) {
        console.error("Results array is undefined or empty");
        return;
    }
    
    
    const initialInvestment = 
        results[0].valueEndOfYear -
        results[0].interest -
        results[0].annualInvestment;

        return (
        <section id="result">
            <h2 className="center">Results</h2>
            <table id="result">
                <thead>
                    <tr>
                        <th>Year</th>
                        <th>Investment Value</th>
                        <th>Interest (Year)</th>
                        <th>Annual Investment</th>
                        <th>Total investment</th>
                    </tr>
                </thead>
                <tbody>
                    {results.map((yearData) => {
                        const totalInterest = 
                            yearData.valueEndOfYear -
                            yearData.annualInvestment * yearData.year -
                            initialInvestment;
                        const totalAmountInvested = 
                            yearData.valueEndOfYear - totalInterest;
                        
                        return (
                        <tr key={yearData.year}>
                            <td>{yearData.year}</td>
                            <td>{formatter.format(yearData.valueEndOfYear)}</td>
                            <td>{formatter.format(yearData.interest)}</td>                    
                            <td>{formatter.format(totalInterest)}</td>
                            <td>{formatter.format(totalAmountInvested)}</td>
                        </tr>
                    );
                    })}
                </tbody>
            </table>
        </section>
    );
}


