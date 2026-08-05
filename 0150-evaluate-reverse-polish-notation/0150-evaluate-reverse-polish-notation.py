class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for token in tokens:
            if not self.isoperator(token):
                st.append(int(token))
            else:
                operand1=st.pop()
                operand2=st.pop()
                result=int(self.res(operand1,operand2,token))
                st.append(result)
        return st[-1]
    def isoperator(self,token):
        return token == "+" or token =="-"  or token == "*" or token == "/"
    def res(self,operand1,operand2,token):
        if token =="+":
            return operand2 + operand1
        elif token == "-":
            return operand2 - operand1
        elif token == "/":
            return operand2 / operand1
        elif token == "*":
            return operand2 * operand1
        else: 
            return None
        
