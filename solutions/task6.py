class Calculation:
    def __init__(self, content):
        self.content = content.split(" ")
    
    def solve(self):
        self.content[0] = int(self.content[0])
        self.content[2] = int(self.content[2])
        match(self.content[1]):
            case("+"):
                return self.content[0] + self.content[2]
            case("-"):
                return self.content[0] - self.content[2]
            case("/"):
                return self.content[0] / self.content[2]
            case("//"):
                return self.content[0] // self.content[2]
            case("*"):
                return self.content[0] * self.content[2]
            case("**"):
                return self.content[0] ** self.content[2]
            case("%"):
                return self.content[0] % self.content[2]
            case("<"):
                return self.content[0] < self.content[2]
            case(">"):
                return self.content[0] > self.content[2]
            case("<="):
                return self.content[0] <= self.content[2]
            case(">="):
                return self.content[0] >= self.content[2]
            case("=="):
                return self.content[0] == self.content[2]
            case("!="):
                return self.content[0] != self.content[2]


exit_code = "leave"
while 1:
    inp = input("Enter your maths: ")
    if inp == exit_code: exit()
    else:
        calculation = Calculation(inp)
        print(calculation.solve())