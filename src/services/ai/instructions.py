parse_instructions = 'you need to generate json blocks from text, it will me used in note taking app, respond using only avalible blocks. respond only in json format. parse text into blocks. for example, if user says they want chicken nuggets generate shopping list and recipe. medium length of text. another example, if user passes mathematical termin you should explain it in blocks and give definition. respond in given language. here example of output, which contains all blocks: [\n  {\n    "id": "af76861a-8d3a-48c5-975d-3e8ec41029f3",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Welcome to this demo!",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "acb055a1-86c5-4870-bfea-9c8d2dfcea5e",\n    "type": "heading",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "level": 1\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "This is a heading block",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "afb972d1-ca23-42b6-889e-0d162667826f",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Text block",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "680aa97f-3937-480a-9cc7-0494f4327efa",\n    "type": "heading",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "level": 2\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Heading 2",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "327e84bc-fec5-4008-9bd0-f0cfc606062b",\n    "type": "heading",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "level": 3\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Heading 3",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "b4842afa-5c73-4730-88ad-badf454a3e39",\n    "type": "numberedListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item 1",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "8c5b7db5-dff6-4a00-99af-fd9519ea6185",\n    "type": "numberedListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item 2",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "b8a07017-eb85-434c-9887-b8b47bab120c",\n    "type": "numberedListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item 3",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "a60f9887-f113-4fb6-a48a-00d18ed027d2",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [],\n    "children": []\n  },\n  {\n    "id": "8db4bbd7-c1a6-44a0-a1a7-0dff7efe0ca8",\n    "type": "bulletListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "8ae58023-fb1f-4f32-be88-2a0b6fd2d16d",\n    "type": "checkListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "checked": false\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "4e9b89db-5b4b-45e7-9ab5-38dbbf7f52bb",\n    "type": "codeBlock",\n    "props": {\n      "language": "javascript"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "console.log(\\"Hello world!);",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "26657dc9-4298-4cc4-ad1d-780e9bd57b2e",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Silly dilly text",\n        "styles": {}\n      }\n    ],\n    "children": [\n      {\n        "id": "8cb7cb29-0e66-48bf-9ee7-c49f596d0805",\n        "type": "paragraph",\n        "props": {\n          "textColor": "default",\n          "backgroundColor": "default",\n          "textAlignment": "left"\n        },\n        "content": [\n          {\n            "type": "text",\n            "text": "level 2 text",\n            "styles": {}\n          }\n        ],\n        "children": []\n      },\n      {\n        "id": "ca103de7-243c-4746-af97-53708c4023d2",\n        "type": "paragraph",\n        "props": {\n          "textColor": "default",\n          "backgroundColor": "default",\n          "textAlignment": "left"\n        },\n        "content": [\n          {\n            "type": "text",\n            "text": "level 2 text",\n            "styles": {}\n          }\n        ],\n        "children": [\n          {\n            "id": "1720b34c-5822-4a59-9762-ac0c15b5877e",\n            "type": "paragraph",\n            "props": {\n              "textColor": "default",\n              "backgroundColor": "default",\n              "textAlignment": "left"\n            },\n            "content": [\n              {\n                "type": "text",\n                "text": "level 3 text",\n                "styles": {}\n              }\n            ],\n            "children": []\n          }\n        ]\n      },\n      {\n        "id": "f6954e04-431d-4947-a64f-efa66aa5b8b7",\n        "type": "paragraph",\n        "props": {\n          "textColor": "default",\n          "backgroundColor": "default",\n          "textAlignment": "left"\n        },\n        "content": [\n          {\n            "type": "text",\n            "text": "level 2 text",\n            "styles": {}\n          }\n        ],\n        "children": []\n      }\n    ]\n  },\n  {\n    "id": "8d49247c-1ed0-496a-9fe6-f2274645168c",\n    "type": "checkListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "checked": false\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "task",\n        "styles": {}\n      }\n    ],\n    "children": [\n      {\n        "id": "bac689aa-f66b-42bc-9031-04fda995495b",\n        "type": "checkListItem",\n        "props": {\n          "textColor": "default",\n          "backgroundColor": "default",\n          "textAlignment": "left",\n          "checked": false\n        },\n        "content": [\n          {\n            "type": "text",\n            "text": "subtask 1",\n            "styles": {}\n          }\n        ],\n        "children": [\n          {\n            "id": "3bd93665-6b7c-4fe1-bd86-f4bf67e28cb7",\n            "type": "checkListItem",\n            "props": {\n              "textColor": "default",\n              "backgroundColor": "default",\n              "textAlignment": "left",\n              "checked": false\n            },\n            "content": [\n              {\n                "type": "text",\n                "text": "subtask 2",\n                "styles": {}\n              }\n            ],\n            "children": [\n              {\n                "id": "9501c7d2-4a44-4da2-8cff-3910576e817d",\n                "type": "checkListItem",\n                "props": {\n                  "textColor": "default",\n                  "backgroundColor": "default",\n                  "textAlignment": "left",\n                  "checked": false\n                },\n                "content": [\n                  {\n                    "type": "text",\n                    "text": "subtask 3",\n                    "styles": {}\n                  }\n                ],\n                "children": []\n              },\n              {\n                "id": "81a6ce54-e23f-4a86-859d-925a0953f5aa",\n                "type": "checkListItem",\n                "props": {\n                  "textColor": "default",\n                  "backgroundColor": "default",\n                  "textAlignment": "left",\n                  "checked": false\n                },\n                "content": [\n                  {\n                    "type": "text",\n                    "text": "subtask 4",\n                    "styles": {}\n                  }\n                ],\n                "children": []\n              },\n              {\n                "id": "33391d9f-ff39-4819-b8db-04cda7ae90e9",\n                "type": "paragraph",\n                "props": {\n                  "textColor": "default",\n                  "backgroundColor": "default",\n                  "textAlignment": "left"\n                },\n                "content": [\n                  {\n                    "type": "text",\n                    "text": "text ",\n                    "styles": {}\n                  }\n                ],\n                "children": []\n              }\n            ]\n          }\n        ]\n      }\n    ]\n  },\n  {\n    "id": "4144df4a-9a52-479c-bc40-f0da677fe27d",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [],\n    "children": []\n  }\n]\n'
summarize_instructions = 'you need to summarize json blocks to json blocks, it will me used in note taking app, respond using only avalible blocks. respond only in json format. you need to summarize given info and optionaly find key ponts. you need to reduce number of words and blocks. respond in given language. here example of output, which contains all blocks: [\n  {\n    "id": "af76861a-8d3a-48c5-975d-3e8ec41029f3",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Welcome to this demo!",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "acb055a1-86c5-4870-bfea-9c8d2dfcea5e",\n    "type": "heading",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "level": 1\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "This is a heading block",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "afb972d1-ca23-42b6-889e-0d162667826f",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Text block",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "680aa97f-3937-480a-9cc7-0494f4327efa",\n    "type": "heading",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "level": 2\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Heading 2",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "327e84bc-fec5-4008-9bd0-f0cfc606062b",\n    "type": "heading",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "level": 3\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Heading 3",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "b4842afa-5c73-4730-88ad-badf454a3e39",\n    "type": "numberedListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item 1",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "8c5b7db5-dff6-4a00-99af-fd9519ea6185",\n    "type": "numberedListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item 2",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "b8a07017-eb85-434c-9887-b8b47bab120c",\n    "type": "numberedListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item 3",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "a60f9887-f113-4fb6-a48a-00d18ed027d2",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [],\n    "children": []\n  },\n  {\n    "id": "8db4bbd7-c1a6-44a0-a1a7-0dff7efe0ca8",\n    "type": "bulletListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "8ae58023-fb1f-4f32-be88-2a0b6fd2d16d",\n    "type": "checkListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "checked": false\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "item",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "4e9b89db-5b4b-45e7-9ab5-38dbbf7f52bb",\n    "type": "codeBlock",\n    "props": {\n      "language": "javascript"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "console.log(\\"Hello world!);",\n        "styles": {}\n      }\n    ],\n    "children": []\n  },\n  {\n    "id": "26657dc9-4298-4cc4-ad1d-780e9bd57b2e",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "Silly dilly text",\n        "styles": {}\n      }\n    ],\n    "children": [\n      {\n        "id": "8cb7cb29-0e66-48bf-9ee7-c49f596d0805",\n        "type": "paragraph",\n        "props": {\n          "textColor": "default",\n          "backgroundColor": "default",\n          "textAlignment": "left"\n        },\n        "content": [\n          {\n            "type": "text",\n            "text": "level 2 text",\n            "styles": {}\n          }\n        ],\n        "children": []\n      },\n      {\n        "id": "ca103de7-243c-4746-af97-53708c4023d2",\n        "type": "paragraph",\n        "props": {\n          "textColor": "default",\n          "backgroundColor": "default",\n          "textAlignment": "left"\n        },\n        "content": [\n          {\n            "type": "text",\n            "text": "level 2 text",\n            "styles": {}\n          }\n        ],\n        "children": [\n          {\n            "id": "1720b34c-5822-4a59-9762-ac0c15b5877e",\n            "type": "paragraph",\n            "props": {\n              "textColor": "default",\n              "backgroundColor": "default",\n              "textAlignment": "left"\n            },\n            "content": [\n              {\n                "type": "text",\n                "text": "level 3 text",\n                "styles": {}\n              }\n            ],\n            "children": []\n          }\n        ]\n      },\n      {\n        "id": "f6954e04-431d-4947-a64f-efa66aa5b8b7",\n        "type": "paragraph",\n        "props": {\n          "textColor": "default",\n          "backgroundColor": "default",\n          "textAlignment": "left"\n        },\n        "content": [\n          {\n            "type": "text",\n            "text": "level 2 text",\n            "styles": {}\n          }\n        ],\n        "children": []\n      }\n    ]\n  },\n  {\n    "id": "8d49247c-1ed0-496a-9fe6-f2274645168c",\n    "type": "checkListItem",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left",\n      "checked": false\n    },\n    "content": [\n      {\n        "type": "text",\n        "text": "task",\n        "styles": {}\n      }\n    ],\n    "children": [\n      {\n        "id": "bac689aa-f66b-42bc-9031-04fda995495b",\n        "type": "checkListItem",\n        "props": {\n          "textColor": "default",\n          "backgroundColor": "default",\n          "textAlignment": "left",\n          "checked": false\n        },\n        "content": [\n          {\n            "type": "text",\n            "text": "subtask 1",\n            "styles": {}\n          }\n        ],\n        "children": [\n          {\n            "id": "3bd93665-6b7c-4fe1-bd86-f4bf67e28cb7",\n            "type": "checkListItem",\n            "props": {\n              "textColor": "default",\n              "backgroundColor": "default",\n              "textAlignment": "left",\n              "checked": false\n            },\n            "content": [\n              {\n                "type": "text",\n                "text": "subtask 2",\n                "styles": {}\n              }\n            ],\n            "children": [\n              {\n                "id": "9501c7d2-4a44-4da2-8cff-3910576e817d",\n                "type": "checkListItem",\n                "props": {\n                  "textColor": "default",\n                  "backgroundColor": "default",\n                  "textAlignment": "left",\n                  "checked": false\n                },\n                "content": [\n                  {\n                    "type": "text",\n                    "text": "subtask 3",\n                    "styles": {}\n                  }\n                ],\n                "children": []\n              },\n              {\n                "id": "81a6ce54-e23f-4a86-859d-925a0953f5aa",\n                "type": "checkListItem",\n                "props": {\n                  "textColor": "default",\n                  "backgroundColor": "default",\n                  "textAlignment": "left",\n                  "checked": false\n                },\n                "content": [\n                  {\n                    "type": "text",\n                    "text": "subtask 4",\n                    "styles": {}\n                  }\n                ],\n                "children": []\n              },\n              {\n                "id": "33391d9f-ff39-4819-b8db-04cda7ae90e9",\n                "type": "paragraph",\n                "props": {\n                  "textColor": "default",\n                  "backgroundColor": "default",\n                  "textAlignment": "left"\n                },\n                "content": [\n                  {\n                    "type": "text",\n                    "text": "text ",\n                    "styles": {}\n                  }\n                ],\n                "children": []\n              }\n            ]\n          }\n        ]\n      }\n    ]\n  },\n  {\n    "id": "4144df4a-9a52-479c-bc40-f0da677fe27d",\n    "type": "paragraph",\n    "props": {\n      "textColor": "default",\n      "backgroundColor": "default",\n      "textAlignment": "left"\n    },\n    "content": [],\n    "children": []\n  }\n]\n'
tags_instructions = None
