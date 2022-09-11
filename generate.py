import pickle
import argparse


def main():
    parser = argparse.ArgumentParser(description="Generate words")
    parser.add_argument("--model", type=str, default=".",
                        help="Path to the directory where the trained model stores")
    parser.add_argument("--length", type=int, default=10,
                        help="Defines the length of generated sequence")
    parser.add_argument("--prefix", type=str, default="",
                        help="Sample to begin generating. Enclose the sentence in quotation marks")
    args = parser.parse_args()

    model_path = args.model
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    print(model.generate(args.length, model.fix_text(args.prefix).split(" ")))


if __name__ == "__main__":
    main()