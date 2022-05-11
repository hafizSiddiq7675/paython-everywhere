import coin

def main():
    # Create an object from the Coin class.
    my_Coin = coin.Coin()
    # Display the side of the coin that is facing up.
    print('This side is up:', my_Coin.get_sideup())
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_Coin.toss()
        print(my_Coin.get_sideup())
# Call the main function.
main()
