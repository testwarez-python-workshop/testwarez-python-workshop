import pytest
from hamcrest import *
from football_example.src.football_manager import FootballManager

league = "PL"
football_manger = FootballManager()


class TestFootball:

    def test_number_of_draws(self):
        num_of_draws = football_manger.get_number_of_results(league, 'x')
        assert_that(num_of_draws, equal_to(100))

    def test_home_vs_away_winnings(self):
        num_of_home_wins = football_manger.get_number_of_results(league, 1)
        num_of_away_wins = football_manger.get_number_of_results(league, 2)
        assert_that(num_of_home_wins, greater_than(num_of_away_wins))


if __name__ == '__main__':
    pytest.main()

