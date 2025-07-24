class EmailService:
    def _connect(self):
        print("connecting to email server")


    def _authenticate(self):
        print("Authenticating...")

    def send_email(self, email):
        self._connect()
        self._authenticate()
        print('sending email')
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server")

email = EmailService()
email.send_email('codegeek004@gmail.com')


