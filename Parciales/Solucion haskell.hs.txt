module Solucion where

-- Problema relacionesValidas
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((p1,p2):rs) = cadaRelValida && noHayRelRep && relacionesValidas rs
                            where 
                                cadaRelValida = p1 /= p2 
                                noHayRelRep = not (pertenece (p1,p2) rs) && not (pertenece (p2,p1) rs) 

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece y (x:xs)
 | y == x = True
 | otherwise = pertenece y xs 


-- Problema personas
personas :: [(String,String)] -> [String]
personas rs = sacarRepes (personasConRepes rs)

personasConRepes :: [(String,String)] -> [String]
personasConRepes [] = []
personasConRepes ((p1,p2):rs) = p1 : p2 : personas rs

sacarRepes :: (Eq t) => [t] -> [t]
sacarRepes [] = []
sacarRepes (x:xs)
 | pertenece x xs = pasoRecursivo
 | otherwise = x : pasoRecursivo
 where pasoRecursivo = sacarRepes xs


-- Problema amigosDe
amigosDe :: String -> [(String,String)] -> [String]
amigosDe _ [] = []
amigosDe p ((p1,p2):rs)  | (p == p1) = p2 : pasoRecursivo
                         | (p == p2) = p1 : pasoRecursivo
                         | otherwise = pasoRecursivo
                         where pasoRecursivo = amigosDe p rs

-- Problema personaConMasAmigos
personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos rs = maximo listaPersonas cantAmigosPersonas
                where
                    listaPersonas      = personas rs
                    cantAmigosPersonas = cantidadDeAmigos listaPersonas rs

cantidadDeAmigos :: [String] -> [(String,String)] -> [Int]
cantidadDeAmigos [] _ = []
cantidadDeAmigos (p:ps) rs = (cantidadDeAmigosDe p rs) : (cantidadDeAmigos ps rs)    

maximo :: [String] -> [Int] -> String
maximo [p] _ = p
maximo (p0:p1:ps) (c0:c1:cs)  | c0 > c1   = maximo (p0:ps) (c0:cs)
                              | otherwise = maximo (p1:ps) (c1:cs)

cantidadDeAmigosDe :: String -> [(String,String)] -> Int
cantidadDeAmigosDe p rs = length (amigosDe p rs)


