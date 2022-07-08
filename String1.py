import logging
logging.basicConfig(filename="String1.log",level=logging.INFO,format='%(levelname)s,%(message)s%(asctime)s')

class String:
    def Isolate(self,a):
        logging.info("Entered text is %s",a)
        try:
            return a[0:300:4]
        except Exception as e:
            logging.error(e)

    def Reverse(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a[::-1]
        except Exception as e:
            logging.error(e)

    def Upper(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.upper()
        except Exception as e:
            logging.error(e)
    def Split(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.split()
        except Exception as e:
            logging.error(e)
    def Lower(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.lower()
        except Exception as e:
            logging.error(e)
    def Capitalize(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.capitalize()
        except Exception as e:
            logging.error(e)
    def Title(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.title()
        except Exception as e:
            logging.error(e)
    def ISALPHANUM(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.isalnum()
        except Exception as e:
            logging.error(e)
    def ISALPHA(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.isalpha()
        except Exception as e:
            logging.error(e)
    def Expandtabs(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.expandtabs()
        except Exception as e:
            logging.error(e)
    def Strip(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.strip()
        except Exception as e:
            logging.error(e)
    def LStrip(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.lstrip()
        except Exception as e:
            logging.error(e)
    def RStrip(self,a):
        logging.info("Entered text is %s", a)
        try:
            return a.rstrip()
        except Exception as e:
            logging.error(e)
    def Replace(self,a):
        logging.info("Entered text is %s", a)
        try:
            z=str(input("Enter the letter to be replaced :"))
            y=str(input("Enter the new letter :"))
            return a.replace(z,y)
        except Exception as e:
            logging.error(e)
    def Center(self,a):
        logging.info("Entered text is %s", a)
        try:
            z=int(input("Space for entering new data before & after the current text :"))
            y=str(input("Enter the new letter :"))
            return a.center(z,y)
        except Exception as e:
            logging.error(e)


c=String()
print(c.Center("ThisismyFirstfunction"))