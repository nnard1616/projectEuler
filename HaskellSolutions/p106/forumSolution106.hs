module Main where
import Data.List
import Control.Monad

main = print $ solve 12

solve n = length $ twoSetsOf [1..n] =<< [2..n`div`2]          
twoSetsOf xs n = do
        firstSet <- setsOf n xs
        let rest = dropWhile (/= head firstSet) xs \\ firstSet
        secondSet <- setsOf n rest
        let f = firstSet  >>= enumFromTo 2
            s = secondSet >>= enumFromTo 2
        guard $ not $ null (f \\ s) || null (s \\ f)
        [()] -- we just need the to count the sets not show them

setsOf (-1) _        = [[]]
setsOf n xs = concat [map (y:) (setsOf (n-1) ys) | (y:ys) <- tails xs]
