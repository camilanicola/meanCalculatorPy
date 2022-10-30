import numpy as np

def calculate(list):
  if(len(list)<9):
    raise ValueError('List must contain nine numbers.')
    
  matriz=np.array(list).reshape(3,3)
  print(matriz)
  ##calculo da media
  matrizMean=matriz.mean().tolist()
  axis0Mean=matriz.mean(axis=0).tolist()
  axis1Mean=matriz.mean(axis=1).tolist()
  ##fim calculo medias

  ##calculo da variancia
  matrizVar=matriz.var().tolist()
  axis0Var=matriz.var(axis=0).tolist()
  axis1Var=matriz.var(axis=1).tolist()
  ##fim calculo variancia

  ##calculo desvio padrao
  matrizDev=matriz.std().tolist()
  axis0Dev=matriz.std(axis=0).tolist()
  axis1Dev=matriz.std(axis=1).tolist()
  ##fim calculo desvio padrao

  ##maior numero
  matrizMax=matriz.max().tolist()
  axis0Max=matriz.max(axis=0).tolist()
  axis1Max=matriz.max(axis=1).tolist()
  ##fim maior numero

  ##menor numero
  matrizMin=matriz.min().tolist()
  axis0Min=matriz.min(axis=0).tolist()
  axis1Min=matriz.min(axis=1).tolist()
  ##fim menor numero

  ##soma 
  matrizSum=matriz.sum().tolist()
  axis0Sum=matriz.sum(axis=0).tolist()
  axis1Sum=matriz.sum(axis=1).tolist()

  return {
     'mean':[axis0Mean,axis1Mean,matrizMean],
     'variance':[axis0Var, axis1Var,matrizVar],
     'standard deviation':[axis0Dev,axis1Dev,matrizDev],
     'max':[axis0Max,axis1Max,matrizMax],
     'min':[axis0Min,axis1Min,matrizMin],
     'sum':[axis0Sum,axis1Sum,matrizSum]
      
   }