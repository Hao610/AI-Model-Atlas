import re
from core.tools.base import BaseTool

class CalculatorTool(BaseTool):
    """A safe math evaluation tool."""
    
    @property
    def name(self) -> str:
        return "calculator"
        
    @property
    def description(self) -> str:
        return "Evaluates basic mathematical expressions."

    def run(self, query: str) -> str:
        # Extract the math part of the string safely
        # Matches numbers, decimals, basic operators, and parentheses
        match = re.search(r'[\d\.\+\-\*\/\^\(\)\s]+', query)
        
        if not match:
            return "Error: No valid math expression found."
            
        expr = match.group(0).strip()
        # Convert ^ to ** for python eval
        expr = expr.replace('^', '**')
        
        # Safety check: ensure no alphabetic characters sneaked in
        if re.search(r'[a-zA-Z]', expr):
            return "Error: Invalid characters in math expression."
            
        try:
            # Safe eval with no builtins or globals
            result = eval(expr, {"__builtins__": {}}, {})
            return str(result)
        except Exception as e:
            return f"Error evaluating expression: {e}"
