class Testcase:


    def __init__(self, inp: str, out: str):
        self.inp = inp
        self.out = out

    def __str__(self) -> str:
        return f"Input:\n{self.inp}\nOutput:\n{self.out}"