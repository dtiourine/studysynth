"use client"

import { useState } from "react"
import { BookOpen, Brain, Play, Eye, MoreHorizontal } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Badge } from "@/components/ui/badge"
import Link from "next/link"

const flashcardSets = [
    {
        id: 1,
        title: "Biology Chapter 12: Cell Division",
        cardCount: 24,
        source: "Biology Chapter 12.pdf",
        created: "2024-01-15",
        difficulty: "Medium",
        preview: [
            { front: "What is mitosis?", back: "The process of cell division that produces two identical diploid cells" },
            { front: "What are the phases of mitosis?", back: "Prophase, Metaphase, Anaphase, Telophase" },
            { front: "What is cytokinesis?", back: "The division of the cytoplasm to form two separate cells" },
        ],
    },
    {
        id: 2,
        title: "History: World War II Timeline",
        cardCount: 18,
        source: "History Notes.docx",
        created: "2024-01-14",
        difficulty: "Easy",
        preview: [
            { front: "When did WWII begin?", back: "September 1, 1939 with Germany's invasion of Poland" },
            { front: "When did the US enter WWII?", back: "December 7, 1941 after Pearl Harbor attack" },
        ],
    },
    {
        id: 3,
        title: "Chemistry: Organic Compounds",
        cardCount: 31,
        source: "Chemistry Formulas.txt",
        created: "2024-01-13",
        difficulty: "Hard",
        preview: [
            { front: "What is the general formula for alkanes?", back: "CnH2n+2" },
            { front: "What functional group defines alcohols?", back: "Hydroxyl group (-OH)" },
        ],
    },
]

const quizSets = [
    {
        id: 1,
        title: "Biology Chapter 12 Quiz",
        questionCount: 15,
        source: "Biology Chapter 12.pdf",
        created: "2024-01-15",
        difficulty: "Medium",
        timeLimit: "20 minutes",
    },
    {
        id: 2,
        title: "History Quiz: WWII Events",
        questionCount: 12,
        source: "History Notes.docx",
        created: "2024-01-14",
        difficulty: "Easy",
        timeLimit: "15 minutes",
    },
]

export default function StudyMaterials() {
    const [selectedSet, setSelectedSet] = useState<number | null>(null)

    const getDifficultyColor = (difficulty: string) => {
        switch (difficulty) {
            case "Easy":
                return "bg-green-100 text-green-800"
            case "Medium":
                return "bg-yellow-100 text-yellow-800"
            case "Hard":
                return "bg-red-100 text-red-800"
            default:
                return "bg-gray-100 text-gray-800"
        }
    }

    return (
        <div className="p-8">
            <div className="max-w-7xl mx-auto">
                <div className="mb-8">
                    <h1 className="text-3xl font-bold text-gray-900 mb-2">Study Materials</h1>
                    <p className="text-gray-600">Review your generated flashcards and quizzes, or start a study session.</p>
                </div>

                <Tabs defaultValue="flashcards" className="space-y-6">
                    <TabsList className="grid w-full max-w-md grid-cols-2">
                        <TabsTrigger value="flashcards" className="flex items-center space-x-2">
                            <BookOpen className="h-4 w-4" />
                            <span>Flashcards</span>
                        </TabsTrigger>
                        <TabsTrigger value="quizzes" className="flex items-center space-x-2">
                            <Brain className="h-4 w-4" />
                            <span>Quizzes</span>
                        </TabsTrigger>
                    </TabsList>

                    <TabsContent value="flashcards" className="space-y-6">
                        <div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
                            {flashcardSets.map((set) => (
                                <Card key={set.id} className="hover:shadow-md transition-shadow">
                                    <CardHeader>
                                        <div className="flex items-start justify-between">
                                            <div className="space-y-2">
                                                <CardTitle className="text-lg">{set.title}</CardTitle>
                                                <div className="flex items-center space-x-2">
                                                    <Badge variant="secondary">{set.cardCount} cards</Badge>
                                                    <Badge className={getDifficultyColor(set.difficulty)}>{set.difficulty}</Badge>
                                                </div>
                                            </div>
                                            <Button variant="ghost" size="sm">
                                                <MoreHorizontal className="h-4 w-4" />
                                            </Button>
                                        </div>
                                        <p className="text-sm text-gray-600">From: {set.source}</p>
                                    </CardHeader>
                                    <CardContent className="space-y-4">
                                        <div className="space-y-2">
                                            <h4 className="text-sm font-medium text-gray-900">Preview:</h4>
                                            {set.preview.slice(0, 2).map((card, index) => (
                                                <div key={index} className="p-2 bg-gray-50 rounded text-xs">
                                                    <p className="font-medium">{card.front}</p>
                                                    <p className="text-gray-600 mt-1">{card.back}</p>
                                                </div>
                                            ))}
                                        </div>
                                        <div className="flex space-x-2">
                                            <Link href={`/study?set=${set.id}&type=flashcards`} className="flex-1">
                                                <Button className="w-full">
                                                    <Play className="h-4 w-4 mr-2" />
                                                    Start Studying
                                                </Button>
                                            </Link>
                                            <Button variant="outline" size="sm">
                                                <Eye className="h-4 w-4" />
                                            </Button>
                                        </div>
                                    </CardContent>
                                </Card>
                            ))}
                        </div>
                    </TabsContent>

                    <TabsContent value="quizzes" className="space-y-6">
                        <div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-6">
                            {quizSets.map((quiz) => (
                                <Card key={quiz.id} className="hover:shadow-md transition-shadow">
                                    <CardHeader>
                                        <div className="flex items-start justify-between">
                                            <div className="space-y-2">
                                                <CardTitle className="text-lg">{quiz.title}</CardTitle>
                                                <div className="flex items-center space-x-2">
                                                    <Badge variant="secondary">{quiz.questionCount} questions</Badge>
                                                    <Badge className={getDifficultyColor(quiz.difficulty)}>{quiz.difficulty}</Badge>
                                                </div>
                                            </div>
                                            <Button variant="ghost" size="sm">
                                                <MoreHorizontal className="h-4 w-4" />
                                            </Button>
                                        </div>
                                        <p className="text-sm text-gray-600">From: {quiz.source}</p>
                                    </CardHeader>
                                    <CardContent className="space-y-4">
                                        <div className="flex items-center justify-between text-sm text-gray-600">
                                            <span>Time limit: {quiz.timeLimit}</span>
                                            <span>Created: {quiz.created}</span>
                                        </div>
                                        <Button className="w-full">
                                            <Play className="h-4 w-4 mr-2" />
                                            Start Quiz
                                        </Button>
                                    </CardContent>
                                </Card>
                            ))}
                        </div>
                    </TabsContent>
                </Tabs>
            </div>
        </div>
    )
}
