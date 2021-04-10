# https://www.interviewbit.com/problems/validating-email-address-using-filter/
def main():
    def check(mail):
        try:
            c = mail.index('@')
            d = mail.index('.')
        except:
            return False
            
        # c=0, d=len(mail)-1,d-c=1 when username, website, extension are not present resp 
        if(c == 0 or d == len(mail)-1 or d-c == 1):
            return False
        if all(list(True if i.isalnum() or i == '-' or i == '_' else False for i in mail[0:c])):
            if all(list(i.isalnum() for i in mail[c+1:d])) and (len(mail) - d - 1)<= 3:
                return True
        return False
        
    N = int(input())
    mails = []
    for i in range(N):
        mails.append(input())
    crct_mails = list(filter(check, mails))
    print(sorted(crct_mails))
    return 0
    
if __name__ == '__main__':
    main()
