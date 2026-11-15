from backend.memory.memory_retriever import MemoryRetriever
from backend.personality.personality import Personality
from backend.character.character_engine import CharacterEngine
from backend.summary.summary_manager import SummaryManager
from backend.relevance.memory_relevance import MemoryRelevance

class PromptBuilder:

    def __init__(self):
        self.memory = MemoryRetriever()
        self.character = CharacterEngine()
        self.summary = SummaryManager()
        self.relevance = MemoryRelevance()

    def build(
        self,
        user_message,
        conversation_history,
        tool_result=None,
        emotion="neutral",
        affinity="new",
        reflection=None,
        style=None
    ):

        # ==========================
        # CHARACTER
        # ==========================

        character_text = self.character.build(
            emotion,
            affinity
        )

        # ==========================
        # LONG TERM MEMORY
        # ==========================

        memories = self.memory.search(user_message)

        memories = self.relevance.filter(
            user_message,
            memories
        )

        if memories:
            memory_text = "\n".join(
                f"- {mem['content']}"
                for mem in memories
            )
        else:
            memory_text = "(Tidak ada memory yang relevan.)"

        # ==========================
        # CONVERSATION SUMMARY
        # ==========================

        summary_text = self.summary.get()

        if not summary_text:

            summary_text = "(Belum ada ringkasan percakapan.)"

        # ==========================
        # SHORT TERM MEMORY
        # ==========================

        recent_history = conversation_history[-10:]

        history_text = ""

        for chat in recent_history:

            role = "User" if chat["role"] == "user" else "Mayumi"

            history_text += f"{role}: {chat['content']}\n"

        # ==========================
        # TOOL RESULT
        # ==========================

        tool_text = ""

        if tool_result:

            tool_text = f"""
=========================
TOOL RESULT
=========================

Tool:
{tool_result["tool_name"]}

Result:
{tool_result["result"]}

Tool sudah berhasil dijalankan.
Jangan mengatakan gagal.
Balas user secara natural sebagai Mayumi.
"""

        # ==========================
        # REFLECTION
        # ==========================

        reflection_text = ""

        if reflection and reflection.get("message"):

            reflection_text = f"""
=========================
REFLECTION
=========================



{reflection["message"]}
"""

        # ==========================
        # CONVERSATION STYLE
        # ==========================

        style_text = ""

        if style and style.get("instruction"):

            style_text = f"""
        =========================
        CONVERSATION STYLE
        =========================

        Ikuti aturan berikut saat menjawab:

        {style["instruction"]}
        """

        # ==========================
        # FINAL PROMPT
        # ==========================

        prompt = f"""
{Personality.SYSTEM_PROMPT}



=========================
LONG TERM MEMORY
=========================

ATURAN PENTING:

- Semua memory di bawah ini adalah fakta yang benar.
- Saat menjawab pertanyaan tentang user, gunakan memory terlebih dahulu.
- Jangan menebak atau mengarang informasi tentang user.
- Jika memory tidak memiliki jawabannya, katakan dengan jujur bahwa kamu tidak mengetahuinya.
- Jika ada konflik antara memory dan percakapan sebelumnya, memory selalu lebih dipercaya.
- Jangan mencampurkan informasi dari personality Mayumi dengan fakta milik user.

Memory yang relevan:

{memory_text}

=========================
CONVERSATION SUMMARY
=========================

Ringkasan percakapan sebelumnya:

{summary_text}



ATURAN:

- Summary ini adalah hasil ringkasan percakapan sebelumnya.
- Gunakan summary untuk menjaga konteks.
- Jangan mengulang pertanyaan yang sudah pernah dijawab.
- Jika informasi ada di summary, gunakan sebagai konteks.

=========================
CURRENT CONVERSATION
=========================

{history_text}

{tool_text}

=========================
CHARACTER STATE
=========================

{character_text}

{style_text}

{reflection_text}



=========================
USER MESSAGE
=========================

{user_message}

=========================
RESPONSE
=========================

Balas sebagai Mayumi secara natural.
"""

        return prompt