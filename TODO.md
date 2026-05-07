# TODO - OCR ParkGuard (precisão máxima + velocidade)

- [x] Revisar `plate-recognition/app.py` atual e identificar regressões (ROI/PSM/threshold/gating).
- [x] Atualizar detecção de ROI: escolher melhor contorno candidato (não retornar imagem inteira) e fallback ordenado.
- [ ] Reduzir chamadas Tesseract mantendo alta precisão: gate por padrões válidos + early exit.
- [ ] Reintroduzir/ajustar pré-processamentos e inversões de forma mais eficiente.
- [ ] Deduplicar resultados e normalizar melhor o OCR (limpeza/pos-filtro).
- [ ] Testar localmente (rodar Flask) com 3–5 imagens e comparar `tempo_processamento` e acurácia.
- [ ] (Se necessário) adicionar endpoint opcional para debug retornando ROI e tempo por etapa.

