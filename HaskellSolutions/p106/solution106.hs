import Data.List

sample12bad = [1..12]

subsets :: [a] -> [[a]]
subsets []     =  [[]]
subsets (x:xs) = subsets xs ++ map (x:)  (subsets xs)
--the same as subsequences from Data.List

disjointPairs :: (Num a, Ord a) => [[a]] -> [[[a]]]
disjointPairs [] = []
disjointPairs (x:xs) = helper x xs ++ disjointPairs xs
                       where
                             helper x []   = []
                             helper x (y:ys) = if (intersect x y == []) && (length x == length y) then [x,y]:(helper x ys) else helper x ys
--takes a list of subsets and returns a list of pairs of disjoint subsets that
--are equal in length.  The only pairs that need to be checked will be of
--subsetss of equal length.

pairListsToOrderings :: Ord a => [[a]] -> [Ordering]
pairListsToOrderings [[], []]         =  []
pairListsToOrderings [(x:xs), (y:ys)] =  (compare x y):(pairListsToOrderings [xs,ys])
--takes a pair of lists of numbers and returns a list of Orderings
--(either LT or GT for each respective element compared)
--Eg: [[2,3],[1,4]]  -> [GT, LT]  (2 is greater than 1 and 3 is less than 4)

allTheSame :: (Eq a1, Num a) => [a1] -> a
allTheSame []       = 0
allTheSame [x]      = 0 
allTheSame (x:y:xs) = if x == y then allTheSame (y:xs) else 1
--takes a list of Orderings and returns 0 if all the same and 1 if not
--Eg: [GT, GT, GT] -> 0
--    [GT, LT, GT] -> 1

main = do
         let dsets = disjointPairs $ tail (subsets sample12bad) 
             answer = sum $ map allTheSame (map pairListsToOrderings dsets )
             --Those that need to be counted have all the same Orderings
         print answer --12.57 seconds
