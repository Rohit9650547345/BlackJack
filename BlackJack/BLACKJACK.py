import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    face_cards = ['jack', 'queen', 'king']

    for suit in suits:
        for card in range(1, 11):
            name = 'cards/{}{}.png'.format(str(card), suit[0])
            image = tkinter.PhotoImage(file=name)  # , height=183, width=120)
            card_images.append((card, image,))

        for card in face_cards:
            name = 'cards/{}{}.png'.format(card[0], suit[0])
            image = tkinter.PhotoImage(file=name)  # , height=183, width=120)
            card_images.append((10, image,))

    '''name = 'cards/1_of_spades.png'
    image = tkinter.PhotoImage(file=name)
    card_images.append((1, image, ))'''


def deal_card(frame):
    next_card = deck.pop()
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    score = 0
    ace = False

    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)

    if player_score > 21:
        result_text.set("Dealer wins !!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins !!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins !!")
    else:
        result_text.set("Draw !!")


def deal_player():
    player_hand.append(deal_card(player_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set('Dealer wins !!')

    '''global player_ace
    global player_score

    next_card = deal_card(player_frame)
    card_value = next_card[0]

    player_hand.append(next_card)

    if card_value == 1 and not player_ace:
        player_ace = True
        card_value = 11
    player_score += card_value

    if player_score > 21 and player_ace:
        player_score -= 10
        player_ace = False
    player_score_label.set(player_score)

    if player_score > 21:
        result_text.set("Dealer wins !!")'''


def new_game():
    global player_hand, dealer_hand, dealer_frame, player_frame, deck

    deck = list(cards)
    random.shuffle(deck)
    result_text.set("")
    dealer_frame.destroy()
    dealer_hand = []
    dealer_frame = tkinter.Frame(card_frame, background='green')
    dealer_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    dealer_hand.append(deal_card(dealer_frame))
    dealer_score = score_hand(dealer_hand)
    dealer_score_label.set(dealer_score)

    player_frame.destroy()
    player_hand = []
    player_frame = tkinter.Frame(card_frame, background='green')
    player_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    deal_player()
    deal_player()


main_win = tkinter.Tk()

main_win.title("BLACKJACK")
main_win.geometry("640x480")
main_win.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(main_win, textvariable=result_text, background='red')
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_win, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

dealer_frame = tkinter.Frame(card_frame, background='green')
dealer_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
# player_ace = False
# player_score = 0

tkinter.Label(card_frame, text="Player", background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

player_frame = tkinter.Frame(card_frame, background='green')
player_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(main_win)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer, width=10, height=2)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=deal_player, width=10, height=2)
player_button.grid(row=0, column=1, sticky='w')

new_game_button = tkinter.Button(button_frame, text='NEW GAME', command=new_game, width=20, height=2)
new_game_button.grid(row=0, column=2)

cards = []
load_images(cards)

deck = list(cards)
random.shuffle(deck)

dealer_hand = []
player_hand = []

deal_player()
dealer_hand.append(deal_card(dealer_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

main_win.mainloop()
