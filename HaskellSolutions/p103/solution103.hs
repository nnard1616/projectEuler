module Solution103 where
import Data.List

deltas = mapM (const [-4..4]) [1..7] --7 dimension displacement vectors with integer components varying from -4..4:
                                     -- [ [-4,-4,-4,-4,-4,-4,-4], [-4,-4,-4,-4,-4,-4,-3],...]

norm :: Floating r => [r] -> r
norm v = sqrt $ sum $ map (^2) v

norms :: (Floating a, Ord a) => [a] -> [a] -> Ordering
norms xs ys  | norm xs < norm ys = LT
             | norm ys < norm xs = GT 
             | otherwise         = EQ

-- GOAL:  Sort list of vectors by their norms (magnitudes)
-- running "sortBy norms norm" yields the following error message:
-- <interactive>:66:8:
--     No instance for (Floating Integer) arising from a use of `norms'
--     In the first argument of `sortBy', namely `norms'
--     In the expression: sortBy norms deltas
--     In an equation for `it': it = sortBy norms deltas
