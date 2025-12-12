"use client";

import { FormEvent, useState } from "react";

type ChatMessage = {
  id: string;
  role: "user" | "assistant";
  content: string;
};

export default function Home() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const onSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const text = input.trim();
    if (!text || isLoading) return;

    // adiciona mensagem do usuário na tela
    const userMessage: ChatMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: text,
    };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
      const resp = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text }),
      });

      if (!resp.ok) {
        const errorMessage: ChatMessage = {
          id: crypto.randomUUID(),
          role: "assistant",
          content:
            "Tive um problema ao falar com o servidor Rios AI. " +
            "Verifique se a API Python está rodando em http://127.0.0.1:8000.",
        };
        setMessages((prev) => [...prev, errorMessage]);
      } else {
        const data = (await resp.json()) as { reply: string };
        const assistantMessage: ChatMessage = {
          id: crypto.randomUUID(),
          role: "assistant",
          content: data.reply,
        };
        setMessages((prev) => [...prev, assistantMessage]);
      }
    } catch (err) {
      console.error(err);
      const errorMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "assistant",
        content:
          "Ocorreu um erro de conexão ao falar com o Rios AI. " +
          "Confira se o backend está ativo.",
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main
      style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#f3f4f6",
        padding: "16px",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: "720px",
          background: "#ffffff",
          borderRadius: "12px",
          boxShadow: "0 2px 10px rgba(0,0,0,0.08)",
          display: "flex",
          flexDirection: "column",
          height: "80vh",
          overflow: "hidden",
        }}
      >
        {/* HEADER */}
        <header
          style={{
            padding: "12px 16px",
            borderBottom: "1px solid #e5e7eb",
            background: "#2563eb",
            color: "white",
          }}
        >
          <h1 style={{ fontSize: "18px", fontWeight: 600 }}>
            Rios AI – Artefact Edition
          </h1>
          <p style={{ fontSize: "13px", opacity: 0.9 }}>
            Olá, pessoal da Artefact! Bem-vindos ao Rios AI. 😊
          </p>
        </header>

        {/* CHAT */}
        <section
          style={{
            flex: 1,
            padding: "12px",
            overflowY: "auto",
            display: "flex",
            flexDirection: "column",
            gap: "8px",
          }}
        >
          {/* estado inicial */}
          {messages.length === 0 && (
            <div style={{ fontSize: "13px", color: "#6b7280" }}>
              Envie uma mensagem para começar. Exemplos:
              <ul style={{ marginTop: "4px", paddingLeft: "18px" }}>
                <li>Quanto é 12 + 35 * 2?</li>
                <li>Qual a cotação do dólar hoje?</li>
                <li>Qual a temperatura de Uberlândia?</li>
                <li>Qual o preço do Bitcoin?</li>
              </ul>
            </div>
          )}

          {/* mensagens */}
          {messages.map((m) => (
            <div
              key={m.id}
              style={{
                display: "flex",
                justifyContent:
                  m.role === "user" ? "flex-end" : "flex-start",
              }}
            >
              <div
                style={{
                  padding: "8px 10px",
                  borderRadius: "10px",
                  maxWidth: "80%",
                  whiteSpace: "pre-wrap",
                  fontSize: "14px",
                  background:
                    m.role === "user" ? "#2563eb" : "#e5e7eb",
                  color: m.role === "user" ? "white" : "#111827",
                }}
              >
                {m.content}
              </div>
            </div>
          ))}

          {isLoading && (
            <div style={{ fontSize: "12px", color: "#9ca3af" }}>
              Rios AI está pensando...
            </div>
          )}
        </section>

        {/* INPUT BAR */}
        <form
          onSubmit={onSubmit}
          style={{
            borderTop: "1px solid #e5e7eb",
            padding: "8px",
            display: "flex",
            gap: "8px",
          }}
        >
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Digite sua mensagem aqui..."
            style={{
              flex: 1,
              padding: "8px 10px",
              borderRadius: "8px",
              border: "1px solid #d1d5db",
              fontSize: "14px",
              outline: "none",
              color: "#111827",          // texto escuro LEGÍVEL
              backgroundColor: "white",  // fundo branco
            }}
          />

          <button
            type="submit"
            disabled={isLoading || !input.trim()}
            style={{
              padding: "8px 12px",
              borderRadius: "8px",
              border: "none",
              background:
                isLoading || !input.trim() ? "#9ca3af" : "#2563eb",
              color: "white",
              fontSize: "14px",
              cursor:
                isLoading || !input.trim()
                  ? "not-allowed"
                  : "pointer",
            }}
          >
            Enviar
          </button>
        </form>
      </div>
    </main>
  );
}
