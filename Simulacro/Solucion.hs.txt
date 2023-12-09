module Solucion where

-- Ejercicio 1
votosEnBlanco :: [(String, String)] -> [Int] -> Int  -> Int
votosEnBlanco _ votos cantTotalVotos = cantTotalVotos - (votosAfirmativos votos)

votosAfirmativos :: [Int] -> Int
votosAfirmativos [] = 0
votosAfirmativos (v:vs) = v + (votosAfirmativos vs) 

-- Ejercicio 2
formulasValidas :: [(String, String)] -> Bool
formulasValidas [] = True
formulasValidas (f:fs) = fst f /= snd f && not (estaEnFormulas (fst f) fs) && not (estaEnFormulas (snd f) fs) && (formulasValidas fs)

estaEnFormulas :: String -> [(String, String)] -> Bool
estaEnFormulas _ [] = False
estaEnFormulas c (f:fs) | c == (fst f) = True
                        | c == (snd f) = True
                        | otherwise = estaEnFormulas c fs

-- = c == (fst f) || c == (snd f) || estaEnFormulas c fs

-- Ejercicio 3
division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos presi fs votos = division (contarVotos presi fs votos) (votosAfirmativos votos)

contarVotos :: String -> [(String, String)] -> [Int] -> Int
contarVotos presi [f] [v] = v
contarVotos presi (f:fs) (v:vs) | presi == fst f = v
                                | otherwise = contarVotos presi fs vs

-- Ejercicio 4
proximoPresidente :: [(String, String)] -> [Int] -> String
proximoPresidente [(presi,_)] _ = presi
proximoPresidente (f1:f2:fs) (v1:v2:vs) | v1 >= v2 = proximoPresidente (f1:fs) (v1:vs)
                                        | otherwise = proximoPresidente (f2:fs) (v2:vs)
  