import argparse
import random


def generate_fake_data(num_lines,
                       file_path,
                       average_house_size,
                       house_size_std,
                       average_price_per_square_feet,
                       price_randomness_range
                       ):
    current_num_lines = 0
    with open(file_path, "w") as fh:
        while current_num_lines < num_lines:
            area = int(random.normalvariate(average_house_size, house_size_std))
            price = int(average_price_per_square_feet*area + price_randomness_range*2*(1 + random.uniform(-1, 1)))
            random_number = random.random()
            if random_number < 0.05:
                fh.write("{:,}".format(area))
            elif 0.05 <= random_number < 0.1:
                fh.write("{:,}\t\t".format(area))
            else:
                fh.write("{:,}\t".format(area))
            fh.write("{:,}\n".format(price))
            current_num_lines += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-lines", "-l", type=int, default=500)
    parser.add_argument("--file-path", "-f",  type=str)
    # Average home size: 2600 square feet (https://money.cnn.com/2014/06/04/real_estate/american-home-size/)
    parser.add_argument("--average-house-size", "-s", type=int, default=1500)
    parser.add_argument("--house-size-std", "-d", type=int, default=500)
    # Median price per square feet: $150 (https://www.zillow.com/home-values/)
    parser.add_argument("--average-price-per-square-feet", "-p", type=int, default=150)
    # Randomness range in price data
    parser.add_argument("--price-randomness-range", "-r", type=int, default=10000)
    args = parser.parse_args()
    generate_fake_data(**vars(args))
