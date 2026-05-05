# Capital Pulse — LinkedIn Header

Banners para o perfil do LinkedIn de João Piccioni, gerados a partir dos design tokens do site `capitalpulse-web` (Sistema Signal v1).

## Arquivos prontos para upload

### Recomendado para uso

- **`linkedin-header-pt-dark-full-1584x396.png`** — versão principal, perfil em português. Eyebrow + manifesto em três linhas + tagline em italic serif. Fundo dark (#0B0D12).

- **`linkedin-header-en-dark-full-1584x396.png`** — versão para perfil em inglês. Mesma estrutura, "Content. / Construction. / Capital." + tagline traduzida.

### Alternativas

- `linkedin-header-pt-dark-minimal-1584x396.png` — sem tagline, masthead maior. Use se quiser respiração visual extra.
- `linkedin-header-pt-paper-full-1584x396.png` — variante paper (fundo creme #FAFAF7). Considerar se quiser destacar do dark default da maioria dos perfis.
- `linkedin-header-pt-paper-minimal-1584x396.png` — paper minimal.
- `linkedin-header-en-dark-minimal-1584x396.png` — minimal em inglês.

### Previews (não para upload — só para conferência)

- `preview-pt-dark-full-with-photo.png` — simula como aparece com a profile photo overlaid no LinkedIn desktop.
- `preview-pt-dark-full-mobile-crop.png` — simula o crop mobile (60% central).
- `preview-pt-dark-minimal-with-photo.png` — minimal com foto.

## Especificação técnica

| Item | Valor |
|---|---|
| Dimensão | 1584 × 396 px (proporção 4:1) |
| Formato | PNG sem perda |
| Cor | sRGB |
| Background dark | #0B0D12 (`--ink-bg`) |
| Background paper | #FAFAF7 (`--paper`) |
| Texto primário (dark) | #F2F1EB (`--text-primary` cream) |
| Texto secundário | #A8AAB4 / #4A4E5A |
| Accent (signal violet) | #5B3BFF |

## Tipografia

| Uso | Fonte | Tamanho |
|---|---|---|
| Eyebrow label | JetBrains Mono Regular | 26px, tracking 0.14em uppercase |
| Manifesto (3 linhas) | Geist SemiBold | 76px (com tagline) / 92px (minimal) |
| Tagline | Instrument Serif Italic | 28px |

Stack idêntico ao do site `capitalpulse-web` (`globals.css`).

## Como subir no LinkedIn

1. Abrir o perfil → ícone de câmera no canto superior direito do banner → "Editar imagem de fundo"
2. Upload do arquivo `linkedin-header-pt-dark-full-1584x396.png`
3. Sem precisar reposicionar — já está no aspect ratio correto
4. Salvar
5. Para a versão em inglês: Configurações → Idioma do perfil → Adicionar inglês → editar perfil em inglês → repetir o upload com `linkedin-header-en-dark-full-1584x396.png`

## Como regerar (se quiser modificar)

```bash
cd /Users/joaopiccioni/Claude-skills/user-skills/capitalpulse-linkedin-header
python3 render.py     # gera os 6 banners
python3 mockup.py     # gera os 3 previews com profile photo overlay
```

Editar `render.py` para mudar texto, cores ou layout. As variáveis principais estão no topo do arquivo (`DARK`, `PAPER`, `MASTHEAD_SIZE_*`, `EYEBROW_SIZE`, `TAGLINE_SIZE`).
