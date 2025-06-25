"use client"

import { useState } from "react"
import { ChevronLeft, ChevronRight, RotateCcw, Check, X, Home } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"
import { Badge } from "@/components/ui/badge"
import Link from "next/link"

const sampleFlashcards = [
    {
        id: 1,
        front: "What is mitosis?",
        back: "The process of cell division that produces two identical diploid cells from a single parent cell. It consists of four dashboard phases: prophase, metaphase, anaphase, and telophase.",
    },
    {
        id: 2,
        front: "What are the phases of mitosis in order?",
        back: "1. Prophase - Chromosomes condense and become visible\n2. Metaphase - Chromosomes align at the cell's equator\n3. Anaphase - Sister chromatids separate and move to opposite poles\n4. Telophase - Nuclear envelopes reform around each set of chromosomes",
    },
    {
        id: 3,
        front: "What is cytokinesis?",
        back: "The division of the cytoplasm that occurs after mitosis, resulting in two separate daughter cells. In animal cells, this happens through the formation of a cleavage furrow.",
    },
    {
        id: 4,
        front: "What is the difference between chromatin and chromosomes?",
        back: "Chromatin is the relaxed, thread-like form of DNA found in the nucleus during interphase. Chromosomes are the condensed, visible form of chromatin that appears during cell division.",
    },
    {
        id: 5,
        front: "What is the purpose of the spindle apparatus?",
        back: "The spindle apparatus is responsible for moving chromosomes during mitosis. It consists of microtubules that attach to kinetochores and help separate sister chromatids during anaphase.",
    },
]

export default function StudySession() {
    const [currentCardIndex, setCurrentCardIndex] = useState(0)
    const [isFlipped, setIsFlipped] = useState(false)
    const [knownCards, setKnownCards] = useState<Set<number>>(new Set())
    const [unknownCards, setUnknownCards] = useState<Set<number>>(new Set())
    const [sessionComplete, setSessionComplete] = useState(false)

    const currentCard = sampleFlashcards[currentCardIndex]
    const progress = ((currentCardIndex + 1) / sampleFlashcards.length) * 100

    const nextCard = () => {
        if (currentCardIndex < sampleFlashcards.length - 1) {
            setCurrentCardIndex(currentCardIndex + 1)
            setIsFlipped(false)
        } else {
            setSessionComplete(true)
        }
    }

    const prevCard = () => {
        if (currentCardIndex > 0) {
            setCurrentCardIndex(currentCardIndex - 1)
            setIsFlipped(false)
        }
    }

    const markAsKnown = () => {
        setKnownCards((prev) => new Set([...prev, currentCard.id]))
        setUnknownCards((prev) => {
            const newSet = new Set(prev)
            newSet.delete(currentCard.id)
            return newSet
        })
        nextCard()
    }

    const markAsUnknown = () => {
        setUnknownCards((prev) => new Set([...prev, currentCard.id]))
        setKnownCards((prev) => {
            const newSet = new Set(prev)
            newSet.delete(currentCard.id)
            return newSet
        })
        nextCard()
    }

    const resetSession = () => {
        setCurrentCardIndex(0)
        setIsFlipped(false)
        setKnownCards(new Set())
        setUnknownCards(new Set())
        setSessionComplete(false)
    }

    if (sessionComplete) {
        return (
            <div className="p-8">
                <div className="max-w-2xl mx-auto text-center">
                    <div className="mb-8">
                        <div className="mx-auto h-16 w-16 bg-green-100 rounded-full flex items-center justify-center mb-4">
                            <Check className="h-8 w-8 text-green-600" />
                        </div>
                        <h1 className="text-3xl font-bold text-gray-900 mb-2">Session Complete!</h1>
                        <p className="text-gray-600">Great job studying Biology Chapter 12: Cell Division</p>
                    </div>

                    <div className="grid grid-cols-2 gap-4 mb-8">
                        <Card>
                            <CardContent className="p-6 text-center">
                                <div className="text-2xl font-bold text-green-600 mb-1">{knownCards.size}</div>
                                <div className="text-sm text-gray-600">Cards Known</div>
                            </CardContent>
                        </Card>
                        <Card>
                            <CardContent className="p-6 text-center">
                                <div className="text-2xl font-bold text-red-600 mb-1">{unknownCards.size}</div>
                                <div className="text-sm text-gray-600">Need Review</div>
                            </CardContent>
                        </Card>
                    </div>

                    <div className="space-y-4">
                        <Button onClick={resetSession} className="w-full">
                            <RotateCcw className="h-4 w-4 mr-2" />
                            Study Again
                        </Button>
                        <Link href="/materials">
                            <Button variant="outline" className="w-full">
                                <Home className="h-4 w-4 mr-2" />
                                Back to Materials
                            </Button>
                        </Link>
                    </div>
                </div>
            </div>
        )
    }

    return (
        <div className="p-8">
            <div className="max-w-4xl mx-auto">
                {/* Header */}
                <div className="mb-8">
                    <div className="flex items-center justify-between mb-4">
                        <div>
                            <h1 className="text-2xl font-bold text-gray-900">Biology Chapter 12: Cell Division</h1>
                            <p className="text-gray-600">
                                Flashcard {currentCardIndex + 1} of {sampleFlashcards.length}
                            </p>
                        </div>
                        <Link href="/materials">
                            <Button variant="outline">
                                <X className="h-4 w-4 mr-2" />
                                Exit
                            </Button>
                        </Link>
                    </div>
                    <Progress value={progress} className="h-2" />
                </div>

                {/* Flashcard */}
                <div className="mb-8">
                    <Card
                        className="min-h-[400px] cursor-pointer transition-all duration-300 hover:shadow-lg"
                        onClick={() => setIsFlipped(!isFlipped)}
                    >
                        <CardContent className="p-8 h-full flex items-center justify-center">
                            <div className="text-center space-y-4">
                                <Badge variant="secondary" className="mb-4">
                                    {isFlipped ? "Answer" : "Question"}
                                </Badge>
                                <div className="text-lg leading-relaxed">
                                    {isFlipped ? (
                                        <div className="whitespace-pre-line">{currentCard.back}</div>
                                    ) : (
                                        <div className="text-xl font-medium">{currentCard.front}</div>
                                    )}
                                </div>
                                {!isFlipped && <p className="text-sm text-gray-500 mt-6">Click to reveal answer</p>}
                            </div>
                        </CardContent>
                    </Card>
                </div>

                {/* Controls */}
                <div className="flex items-center justify-between">
                    <Button variant="outline" onClick={prevCard} disabled={currentCardIndex === 0}>
                        <ChevronLeft className="h-4 w-4 mr-2" />
                        Previous
                    </Button>

                    {isFlipped && (
                        <div className="flex space-x-4">
                            <Button variant="outline" onClick={markAsUnknown} className="border-red-200 text-red-700 hover:bg-red-50">
                                <X className="h-4 w-4 mr-2" />
                                Need Review
                            </Button>
                            <Button onClick={markAsKnown} className="bg-green-600 hover:bg-green-700">
                                <Check className="h-4 w-4 mr-2" />
                                Got It!
                            </Button>
                        </div>
                    )}

                    <Button onClick={nextCard} disabled={currentCardIndex === sampleFlashcards.length - 1 && !isFlipped}>
                        Next
                        <ChevronRight className="h-4 w-4 ml-2" />
                    </Button>
                </div>

                {/* Progress Stats */}
                <div className="mt-8 grid grid-cols-3 gap-4 text-center">
                    <div>
                        <div className="text-2xl font-bold text-gray-900">{currentCardIndex + 1}</div>
                        <div className="text-sm text-gray-600">Current</div>
                    </div>
                    <div>
                        <div className="text-2xl font-bold text-green-600">{knownCards.size}</div>
                        <div className="text-sm text-gray-600">Known</div>
                    </div>
                    <div>
                        <div className="text-2xl font-bold text-red-600">{unknownCards.size}</div>
                        <div className="text-sm text-gray-600">Review</div>
                    </div>
                </div>
            </div>
        </div>
    )
}
