// app/api/chat/route.ts
import { NextRequest, NextResponse } from "next/server";

const PYTHON_API_URL = "http://127.0.0.1:8000/chat";

export async function POST(req: NextRequest) {
  const { message } = (await req.json()) as { message?: string };

  const text = (message ?? "").trim();

  if (!text) {
    return NextResponse.json(
      { reply: "Não recebi nenhuma mensagem de texto para responder." },
      { status: 400 }
    );
  }

  try {
    const resp = await fetch(PYTHON_API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    if (!resp.ok) {
      return NextResponse.json(
        {
          reply:
            "Tive um problema ao falar com o servidor Rios AI em Python. " +
            "Verifique se ele está rodando em http://127.0.0.1:8000/chat.",
        },
        { status: 500 }
      );
    }

    const data = (await resp.json()) as { reply: string };

    return NextResponse.json({ reply: data.reply });
  } catch (err) {
    console.error("Erro ao chamar o backend Python:", err);
    return NextResponse.json(
      {
        reply:
          "Ocorreu um erro de conexão com o servidor Rios AI. " +
          "Confirme se ele está ativo e acessível.",
      },
      { status: 500 }
    );
  }
}
