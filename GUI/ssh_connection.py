import paramiko
import time
import re


class SshCommunication:
    def __init__(self):
        self._hostname = ""    # hostname is your raspberry pi ip address
        self._username = ""
        self.connected = False
        self._passwd_auth = False
        # Initialize the SSH client
        self.client = paramiko.SSHClient()

        # Add the server's host key automatically without prompting
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, value):
        if not value:
            raise ValueError("Hostname cannot be empty.")
        else:
            # Regex pattern for matching an IPv4 address
            pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
            if not value or not re.match(pattern, value):
                raise ValueError("Invalid hostname. Please provide a valid IP address in the format XXX.XXX.XXX.XXX, where each XXX is a number between 0 and 255.")
            self._hostname = value
        

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Username cannot be empty.")
        self._username = value

    @property
    def passwd_auth(self):
        return self._passwd_auth

    @passwd_auth.setter
    def passwd_auth(self, value):
        if not isinstance(value, bool):
            raise ValueError("passwd_auth must be a boolean value.")
        self._passwd_auth = value



    def connect(self, passwd_key):

        try:
            if self._passwd_auth:
                # Connect to the Raspberry Pi
                self.client.connect(hostname = self.hostname, username = self.username, password = passwd_key)
                self.connected = True

            else:
                key = paramiko.RSAKey.from_private_key_file(passwd_key)
                
                self.client.connect(self.hostname, username=self.username, pkey=key)
                self.connected = True
                print("Connected successfully")
        except Exception as e:
            return f"Failed to establish connection with the specified device: {e}"


    def execute_command(self,cmd_list):
            try:
                # Execute a command list
                channel = self.client.invoke_shell()
                ##Opens a shell and keeps the context, it does not restart the session when a new command is executed
                for command in cmd_list:
                    channel.send(command + "\n")
                    time.sleep(1)  # Adjust based on command execution time

                    """# Receive output 
                    while not channel.recv_ready():  # Wait for the command to execute
                        time.sleep(0.5)
                    output = channel.recv(65535).decode('utf-8')  # Adjust buffer size if necessary
                    print(output)""" #Uncomment if the output is needed

                # Close the channel
                channel.close()
            


            except Exception as e:
                print(f"Failed to execute command: {e}")
                
    def close_connection(self):
        try:
            # Close the connection
            self.client.close()
            self.connected = False
        except Exception as e:
            print(f"Something went wrong, couldn't close de ssh connection: {e}")