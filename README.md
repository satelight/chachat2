# FastAPI OpenAI Proxy

このプロジェクトは、FastAPI を使って OpenAI API に非同期でアクセスするサンプルです。

## 構成

- Python + FastAPI
- 非同期 HTTP クライアント: httpx
- エンドポイント: `/chat`

## 前提条件

- Python 3.8 以上
- OpenAI APIキーを保持していること

## セットアップ手順

1. リポジトリをクローン

```bash
git clone <your-repo-url>
cd backend
uvicorn main:app --reload

# sv

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npx sv create

# create a new project in my-app
npx sv create my-app
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.
