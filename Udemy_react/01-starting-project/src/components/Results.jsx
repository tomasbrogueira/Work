import { calculateInvestmentResults } from "../util/investment";

export default function Results({ userInput }) {
    const results = calculateInvestmentResults(userInput);
    
    return (
        <section id="result">
        <h2 className="center">Results</h2>
        <table>
            <thead>
            <tr>
                <th>Year</th>
                <th>Interest Earned</th>
                <th>Investment Value</th>
                <th>Annual Investment</th>
            </tr>
            </thead>
            <tbody>
            {results.map((result) => (
                <tr key={result.year}>
                <td>{result.year}</td>
                <td>{result.interest}</td>
                <td>{result.valueEndOfYear}</td>
                <td>{result.annualInvestment}</td>
                </tr>
            ))}
            </tbody>
        </table>
        </section>
    );
}


