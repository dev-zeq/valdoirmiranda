# Valdoir Miranda

Site estático multilíngue do projeto Código da Longevidade.

## Estrutura

- `index.html`: página principal em português.
- `en/` e `es/`: versões em inglês e espanhol.
- `assets/module.js`: comportamento compartilhado das páginas de conteúdo.
- `build_i18n.py`: gera as versões traduzidas da página principal.
- `sw.js` e `manifest.json`: recursos do aplicativo web instalável. As páginas
  e os arquivos em `assets/` são buscados na rede primeiro (o cache só entra
  offline), então mudanças em `assets/module.js` chegam aos alunos sem precisar
  trocar o `CACHE_NAME`. Só é preciso subir o `CACHE_NAME` ao mudar a lista
  `PRECACHE_URLS` ou os ícones.
- `infra/`: configuração e scripts de implantação.

## Gerar as páginas traduzidas

O script resolve os caminhos a partir da própria pasta do projeto e pode ser
executado em qualquer ambiente:

```bash
python3 build_i18n.py
```

Revise os avisos `WARN` exibidos pelo script antes de publicar as páginas
geradas.
