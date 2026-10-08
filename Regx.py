{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP4PO7ylD76sN/fxlPb8aJN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/PratikshaYadav8799/Python_Programming/blob/main/Regx.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "46mutd5YGP_D",
        "outputId": "52513074-8e4e-445a-ccdc-8eb69eff5740"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 10\n",
            "This statement executes when no exception occurs\n",
            "Done\n"
          ]
        }
      ],
      "source": [
        "try:\n",
        "  x=int(input(\"Enter a number: \"))\n",
        "\n",
        "except Exception as e:\n",
        "  print(\"Exceptions occured {e}\")\n",
        "\n",
        "else:\n",
        "  print(\"This statement executes when no exception occurs\")\n",
        "\n",
        "finally:\n",
        "  print('Done')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import logging\n",
        "logging.basicConfig(level = logging.INFO,\n",
        "                    filename='model.log',\n",
        "                    filemode='w',\n",
        "                    format=\"%(asctime)s - %(message)s - %(levelname)s\",\n",
        "                    force=True)\n",
        "\n",
        "try:\n",
        "  x=int(input('Enter a number: '))\n",
        "except Exception as e:\n",
        "  logging.exception('Please check the entered number: ')\n",
        "else:\n",
        "  logging.info('The value entered successfully')\n",
        "finally:\n",
        "   logging.info(\"Done with all the steps\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Iy-Cw-1KJ-EY",
        "outputId": "ffc436a2-8b69-4e37-8304-4b34e791d010"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter a number: 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  num1=int(input('Enter first number: '))\n",
        "  num2=int(input('Enter second number: '))\n",
        "  num3=num1/num2\n",
        "except ValueError:\n",
        "  print(\"Check the entered value\")\n",
        "except:\n",
        "  #logging.exception(\"Check the values\")\n",
        "  print(\"Check the values\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WPBZfjzaOurX",
        "outputId": "472afe1d-55b9-48d8-b8f1-57d73702719e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: abc\n",
            "Check the entered value\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "text_to_search = \"\"\"I am learning Python and I am enjoying it\"\"\"\n",
        "\n",
        "#want to search all appearance of a\n",
        "\n",
        "pattern = re.compile(r'a')\n",
        "Matches = pattern.finditer(text_to_search)\n",
        "for match in Matches:\n",
        "  print(match)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hIGuAwtNYQk0",
        "outputId": "5a0794e8-01c1-4eea-b688-354665485576"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<re.Match object; span=(2, 3), match='a'>\n",
            "<re.Match object; span=(7, 8), match='a'>\n",
            "<re.Match object; span=(21, 22), match='a'>\n",
            "<re.Match object; span=(27, 28), match='a'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "text_to_search=\"\"\"Hi Hello Namaste\"\"\"\n",
        "\n",
        "pattern=re.compile(r'e')\n",
        "Matches=pattern.finditer(text_to_search)\n",
        "for match in Matches:\n",
        "  print(match)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FitxCgdTcKrK",
        "outputId": "49ab72c1-0238-4aeb-d9f5-c0315b837091"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<re.Match object; span=(4, 5), match='e'>\n",
            "<re.Match object; span=(15, 16), match='e'>\n"
          ]
        }
      ]
    }
  ]
}