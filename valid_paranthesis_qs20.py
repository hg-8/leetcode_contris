class solution:
    def isvalid(self,s:str)->bool:
        st=[]
        for ch in s:
            if self.isopening(ch):
                st.append(ch)
            else:
                if len(st)==0:
                    return False
                else:
                    if (self.ismatch(st[-1],ch)):
                        st.pop()
                    else:
                        return False
        if len(st)==0:
            return True
        else:
            return False
    def isopening(self,ch):
        return ch == '(' or ch== '{' or ch=='['
    def ismatch(self,och,cch):
        return (och =='(' and cch == ')') or (och == '{' and cch =='}') or (och =='[' and cch ==']')
    
