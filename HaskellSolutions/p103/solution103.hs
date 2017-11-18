module Solution103 where
import Data.List

deltas = mapM (const [-4..4]) [1..7] --how does mapM work?

norm v = sqrt $ sum $ map (^2) v

norms xs ys  | norm xs < norm ys = LT
             | norm ys < norm xs = GT 
             | otherwise         = EQ



