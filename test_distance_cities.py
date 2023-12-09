import distance_cities as cs
from click.testing import CliRunner


# def test_cities_cli():
#     citi=['Seattle','Houston']

#     re=cs.my_cities(citi)
#     print(re)


def test_cities_cli():
    # Create a CliRunner instance
    runner = CliRunner()

    # Define your city list
    cities = ["Seattle", "Houston"]

    # Use invoke to simulate the command-line call
    result = runner.invoke(cs.cities_cli, cities)

    print("\ntest result is ", result.output)

    # Check if the command was successful
    assert result.exit_code == 0

    # Print the result
