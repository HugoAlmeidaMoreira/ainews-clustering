# Recovering original data

- The original vectors can be reconstructed using its principal components
- Given the reduced data space, how to retrieve/decompress old data?

DataRecovered = (FeatureVector × TransformedData) + OriginalMean

```vba
we did: TransformedData = FeatureVector^T × DataAdjust^T
so we can do: DataAdjust^T = (FeatureVector^T)^{-1} × TransformedData
(orthogonal property) = FeatureVector × TransformedData
and: DataRecovered = DataAdjust + OriginalMean
```

41

TÉCNICO+

FORMAÇÃO AVANÇADA