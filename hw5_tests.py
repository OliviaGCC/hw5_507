#########################################
##### Name: <Chenchen Gao> #####
##### Uniqname:<gaochenc>#####
#########################################




import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)   #diamond2
        c2 = hw5_cards.Card(1, 1)   # clubs1

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c3 = hw5_cards.Card(0, 12)
        self.assertEqual(c3.rank,12)
        self.assertIsInstance(c3.rank,int)
        X = c3.rank_name
        Y = "Queen"
        self.assertEqual(X, Y)
        return X, Y
        
    
    def test_q2(self):
        '''
        1. fill in your test method for question 2:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c4 = hw5_cards.Card(1,rank = 2)
        self.assertEqual(c4.suit, 1)
        X = c4.suit_name
        Y = "Clubs"
        self.assertEqual(X, Y)

        return X, Y    
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c5 = hw5_cards.Card(3,13)
        X = c5.__str__()
        Y = "King of Spades"
        self.assertEqual(X, Y)
        
        return X, Y
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c6 = hw5_cards.Deck()
        X = len(c6.cards) # c6 does not have len, but c6.cards has
        Y = 52
        self.assertEqual(X, Y)
        return X, Y

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c7 = hw5_cards.Deck()
        X = c7.deal_card() # deal the top card "King of Spades"
        Y = hw5_cards.Card
 
        self.assertIsInstance (X, Y)

        return  X, Y
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c7 = hw5_cards.Deck()
        Y = 51
        Deck_after = c7.deal_card() #Deck after deal 1 card has 51 left
        X =len(c7.cards)
        self.assertEqual (X, Y)

        return  X, Y    
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c7 = hw5_cards.Deck()
        Deal1 = c7.deal_card() 
        X = len(c7.cards)+1
        c7.replace_card(Deal1) #put top card back to deck
        Y = len(c7.cards)
        Z = 52
        self.assertEqual (X,Y)
        return X, Y, Z
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command

        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        c7 = hw5_cards.Deck()  
        Deal1 = c7.deal_card(5)  # deal the 5th from deck c7
        X = len(c7.cards) + 1

        c8 = hw5_cards.Deck()   # create another deck
        Deal2 = c8.deal_card(4) # deal the 4th from this deck c8

        c7.replace_card(Deal2)  # replace the 4th from deck c8 to deck c7, replace_card function should not allow because this card already in it
        Y = len(c7.cards) + 1
        self.assertEqual (X,Y)
        return X, Y



if __name__=="__main__":
    unittest.main()