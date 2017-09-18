# coding: utf-8

class Book:
    def __init__(self, title, author, year, summary):
        self.title = title
        self.author = author
        self.year = year
        self.summary = summary

# dummy data
_books = []
_books.append(Book('Steppenwolf', 'Hermann Hesse', 1927, 'Harry Haller, a middle-aged intellectual, moves into a lodging house in a medium-sized, generic town, which is never named. Despairing and melancholy, Harry feels himself to be "a wolf of the Steppes," or "Steppenwolf," adrift and alone in a world that is incomprehensible to him and offers him no joy. Steppenwolf recounts Harry\'s pain and anxiety as he tries to overcome his crippling sense of dislocation and despair at the futility of humanity.'))
_books.append(Book('Siddhartha', 'Hermann Hesse', 1922, 'Siddhartha, the handsome and respected son of a Brahmin, lives with his father in ancient India. Everyone in the village expects Siddhartha to be a successful Brahmin like his father. Siddhartha enjoys a near-idyllic existence with his best friend, Govinda, but he is secretly dissatisfied. He performs all the rituals of religion, and he does what religion says should bring him happiness and peace. Nonetheless, he feels something is missing. His father and the other elders have still not achieved enlightenment, and he feels that staying with them will not settle the questions he has about the nature of his existence. Siddhartha believes his father has already passed on all the wisdom their community has to offer, but he longs for something more.'))
_books.append(Book('The Master and Margarita', 'Mikhail Bulgakov', 1966, 'The Master and Margarita presents three interlaced lines of action, which are integrated and are mutually enlightening: a visit by Satan to Moscow, a Faustian love story of a writer and his Margarita, and Pilate\'s condemnation of Jesus to execution. The Moscow and Jerusalem episodes have parallels, and the love story connects the two.'))
_books.append(Book('Heart of a Dog', 'Mikhail Bulgakov', 1925, u'"The Heart of a Dog" is one of the best examples of Bulgakov\'s criticism of life in the Soviet Union. According to different views after final analysis it was apprehended as an absurd and satirical story. The novel was written and introduced in March 1925 in one of the Moscow apartments, where had gathered approximately 50 intellectuals of that time. After this event Bulgakov\'s flat was searched and his personal diary and the other works, including our novel, were confiscated because of its provocative character. The result — prohibition of the writer\'s plays in all theatres. Just four years later it was returned to the author and Mikhail Opanasovich\'s plays were back just in the Moscow Art Theatre. After that "The Heart of a Dog" was widely read in samizdat — unofficial publication of literary works.'))

def Get_Books():
    return _books

def Filter_Books(search_string):
    search_string = search_string.lower()
    books = filter(lambda x: (
          search_string in x.author.lower() or
          search_string in x.title.lower()
        ) , _books)
    return books

def Get_Book(author, title):
    return filter(lambda book: (
        author == book.author and
        title == book.title
    ), _books)[0]
