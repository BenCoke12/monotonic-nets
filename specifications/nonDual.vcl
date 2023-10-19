--non dual specification for regression network
--try: x > 0.5 => f(x) > 0.4

--define valid input
validInput : Vector Rat 1 -> Bool
validInput inVal = 0 <= inVal ! 0 <= 1

--input and output types
type InValue = Vector Rat 1
type OutValue = Vector Rat 1

--define regression network
@network
regression : InValue -> OutValue

@property
--high in implies high out
highInHighOut : Bool
highInHighOut = forall x . 
    validInput x and x ! 0 >= 0.5 => regression x ! 0 >= 0.5

@property
--valid input implies valid output
validInValidOut : Bool
validInValidOut = forall x . validInput x => validInput (regression x)