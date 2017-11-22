import Data.List
import Data.List.Split

sample5 = [8, 9, 11, 12, 13]

qualifier ::(Num a, Ord a ) => [a] -> [a] -> Bool
qualifier y x = 
   case intersect y x == []  of 
         True ->   ( if l_a > l_b then s_a > s_b else if l_a < l_b then  s_a < s_b else s_a /= s_b ) 
                   where 
                        s_a = sum y 
                        s_b = sum x 
                        l_a = length y
                        l_b = length x 
         _    -> True

subset::[a] ->[[a]]
subset [] = [[]]
subset (x:xs) = subset xs ++ map (x:)  (subset xs)
 
checkSpecial :: (Num a, Ord a) => [a] -> Bool
checkSpecial xs = specialHelper (sortBy (\x y -> compare (sum x) (sum y)) (subset xs))
                  where
                        specialHelper [x,y] = qualifier x y
                        specialHelper (x:y:xs) = if qualifier x y then specialHelper (y:xs) else False

main = do
       fileContents <- fmap lines . readFile $ "./p105_sets.txt"
       let sets = map (map (\x -> read x :: Int)) $ map (splitOn ",") fileContents 
           answer = sum $ map (\x -> if checkSpecial x then sum x else 0) sets
       print answer
