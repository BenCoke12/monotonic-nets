--input and output types
type InValue = Vector Rat 1
type OutValue = Vector Rat 1

--define valid input
validInput : Vector Rat 1 -> Bool
validInput inVal = 0 <= inVal ! 0 <= 1

--define network as function from inputs to outputs (rationals)
--define regression network
@network
regression : InValue -> OutValue

--monotonic increase
@property
monotonicIncrease : Bool
monotonicIncrease = 
    forall i .
        forall j .
            (validInput i and validInput j) and i ! 0 <= j ! 0 => regression i ! 0 <= regression j ! 0