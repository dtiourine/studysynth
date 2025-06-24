import type React from "react"
import type { Metadata } from "next"
import { Inter } from "next/font/google"
import "./globals.css"
import { Sidebar } from "@/components/sidebar"

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
    title: "StudySynth - AI-Powered Study Tool",
    description: "Generate flashcards and quizzes from your study materials",
}

export default function RootLayout({
                                       children,
                                   }: {
    children: React.ReactNode
}) {
    return (
        <html lang="en">
        <body className={inter.className}>
        <div className="flex min-h-screen bg-gray-50">
            <Sidebar />
            <main className="flex-1 overflow-auto">{children}</main>
        </div>
        </body>
        </html>
    )
}
