module Solution103 where
import Data.List

start7 = [22,33,39,42,44,45,46]
start5 = [6,9,11,12,13]
deltas = mapM (const [-4..4]) [1..7] --7 dimension displacement vectors with integer components varying from -4..4:
                                     -- [ [-4,-4,-4,-4,-4,-4,-4], [-4,-4,-4,-4,-4,-4,-3],...]

norm :: [Integer] -> Float
norm v = sqrt $ fromIntegral $ sum $ map (^2) v

sortByNorms :: [[Integer]] -> [[Integer]] --uses merge sort
sortByNorms = sortBy compareVects 
            where compareVects a b = norm a `compare` norm b

sortBySums :: [[Integer]] -> [[Integer]]
sortBySums = sortBy compareVects
           where compareVects a b = sum a `compare` sum b

sumVects :: Num b => [a] -> [b] -> [b]
sumVects v1 v2 = map sum $ zip v1 v2

subset :: [a] -> [[a]]
subset [] = [[]]
subset (x:xs) = subset xs ++ map (x:) (subset xs)

combination :: [a] -> Int -> [[a]]
combination _   0    = [[]]
combination []  _    = []
combination (x:xs) n = ( map (x:)  (combination xs (n-1)) ) ++ combination xs n

folder x y = if sum x == sum y || y == [-1] then [-1] else [sum y]
