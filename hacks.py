###Diffculty: Training###
###accepted output: 3 integers, the third is four times the sum of the first two###
puzzle1 = ['Other IPs.txt',
('get'),
('cop',-1,1),
('get'),
('cop',-1,2),
('get'),
('cop',-1,3),
('ad','n1',4,'n12'),
('ad',1,2,'n4'),
('comp',2,3),
('ad','n0',-1,-1),
('ad',-1,4,'n1'),
('goto',4),
('win',0),
('lose')
]  

###Difficulty: Easy###
###accepted output. Positive, second triples the first###
puzzle2 = ['Case files.txt',
('output','Enter a positive integer'),
('get'),
('cop',-1,0),
('comp',0,'n0'),
('ad','n0',0,'n3'),
('cop',-1,1),
('cop',-1,2),
('ad','n0',1,1),
('ad',1,2,'n-4'),
('ad','n19',2,'n1'),##
('goto',2),
('output','Enter another positive integer'),#11
('get'),
('ad',-1,3,'n1'),
('comp',0,3),
('ad',-1,4,-1),
('ad','n18',4,'n1'),
('goto',4),
('win',0),
('lose')]#19

###Difficulty: Easy###
###accepted output: x=439. y*z between 1000 and 1100
puzzle3 = ['puzzle3Clue',
('output','Please enter password number 1'),
('get'),
('comp',-1,'n439'),
('ad','n6',-1,'n1'),
('goto',-1),
('lose'),
('goto','n8'),
('lose'),
('output','Password accepted, enter a number'),
('get'),
('cop',-1,0),
('output','Enter one more number'),
('get'),
('cop',-1,1),
('ad','n0',0,1),
('comp',0,'n1000'),
('cop',-1,1),
('comp',0,'n1100'),
('ad',-1,1,'n1'),
('comp','n0',1),
('ad','n23',-1,'n1'),
('goto',-1),
('lose'),
('win',0),
('lose')
]

###Difficulty: Moderate###
###input plugged into -3*x^2+1110x (factored: -3x(x-370))  derivative = -6x+1110= -8(x-185)###
###Successful output: getting the maximum output. Partial success: getting a very high output###
p4 = ['puzzle4clue',
('output', 'Please enter a number'),
('get'),
('cop',-1,0),
('ad',0,5,'n-3'),
('ad','n0',5,0),
('ad','n0',0,'n1110'),
('ad',0,5,'n1'),
('comp',5,'n102675'),
('cop',-1,0),
('comp',5,'n102600'),
('cop',-1,1),
('ad',0,1,'n1'),
('ad','n16',1,'n1'),
('goto',1),
('lose'),
('lose'),
('win',1),
('win',0),
]

###Difficulty: Moderate###
###Takes in three numbers. Outputs a win if the first to the power of the second is the third.###
###Input is limited in the ways described within the program.###
p5 = ['puzzle5clue',
('output', 'Please enter a number between 3 and 15 inclusive'),
('get'),
('cop',-1,0),
('comp',0,'n2'),
('cop',-1,1),
('comp',0,'n16'),
('ad',-1,1,'n1'),
('comp',1,'n0'),
('cop',-1,1),
('ad','n0',1,1),
('ad','n0',1,'n-1'),
('ad','n14',1,'n1'),
('goto',1),#12
('lose'),
('output', 'Please enter another number between 3 and 15 inclusive'),
('get'),
('cop',-1,2),
('comp',2,'n2'),
('cop',-1,1),
('comp',2,'n16'),
('ad',-1,1,'n1'),
('comp',1,'n0'),
('cop',-1,1),
('ad','n0',1,1),
('ad','n0',1,'n-1'),
('ad','n28',1,'n1'),
('goto',1),#26
('lose'),
('output', 'Please enter any number'),
('get'),
('cop',-1,3),
('cop',0,4),
('ad','n-2',2,'n1'),
('comp',2,'n0'),
('ad','n0',0,4),
('ad','n0',-1,-1),
('ad','n0',-1,'n-7'),
('ad','n40',-1,'n1'),
('ad','n-1',2,'n1'),
('goto',-1),#39
('comp',3,0),
('ad','n44',-1,'n1'),
('goto',-1),
('lose'),
('win',0),
('lose')
]



puzzles = [puzzle1, puzzle2, puzzle3, p4, p5]
