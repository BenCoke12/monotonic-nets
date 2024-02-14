--non dual specification for regression network
--try: x > 0.5 => f(x) > 0.4

--define valid input
validInput : Vector Rat 1 -> Bool
validInput inVal = 0 <= inVal ! 0 <= 1

--input and output types
type InValue = Vector Rat 1
type OutValue = Vector Rat 1

--define regression network
--1nYeX is a simple f(x) = ReLU(1*x+0) network
@network
regression : InValue -> OutValue

-- @property
--f(x) exists forall valid x
--not allowed to put an exists and a forall in one property
--existence : Bool
--existence = forall x . validInput x => exists (regression x)

@property
--high in implies high out
highInHighOut : Bool
highInHighOut = forall x . 
    validInput x and x ! 0 >= 0.5 => regression x ! 0 >= 0.49

-- @property
--valid input implies valid output
--validInValidOut : Bool
--validInValidOut = forall x . validInput x => validInput (regression x)

-- @property
--x == y
--does not compile, issue 74
--inEqualsOut : Bool
--inEqualsOut = forall x . validInput x => x ! 0 == (regression x) ! 0