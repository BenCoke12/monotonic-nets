--max of two values
max : Rat -> Rat -> Rat
max a b = if a >= b then a else b

--absolute value of a number
abs : Rat -> Rat
abs n = max n (-n)

--limit of function
--lim : 
--lim f a = 
    --forall x .
    --0 <= abs(x - a) < delta => abs(f x - L) < epsilon

--continuity
-- a function in continuous over a domain if forall points in the domain 
-- f(x) is exists
-- the limit of f(x) as x -> is f(a)
--left and right approach

--intermediate value theorem
--function takes on every value between the max and min value within the domain

--lipschitz continuousness
@parameter
Lip : Rat

@network
regression : Vector Rat 1 -> Vector Rat 1

--define valid input
validInput : Vector Rat 1 -> Bool
validInput inVal = 0 <= inVal ! 0 <= 1

@property
lipschitz : Bool
lipschitz = forall x y . validInput x and validInput y =>
    abs(regression x ! 0 - regression y ! 0) <= Lip * abs(x ! 0 - y ! 0)