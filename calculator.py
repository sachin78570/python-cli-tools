import argparse

parser = argparse.ArgumentParser(description="Simple CLI Calculator")
parser.add_argument("a", type=float, help="First number")
parser.add_argument("b", type=float, help="Second number")
parser.add_argument("operation", type=str, choices=["add", "sub", "mul", "div"], help="Operation")

args = parser.parse_args()

if args.operation == "add":
    result = args.a + args.b
elif args.operation == "sub":
    result = args.a - args.b
elif args.operation == "mul":
    result = args.a * args.b
elif args.operation == "div":
    result = args.a / args.b

print("Result:", result)
