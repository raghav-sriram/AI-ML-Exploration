# Raghav Sriram
# Thursday, October 26th, 2023
# Machine Learning 1 Gabor
# Prompt Generation Short Story Lab
# Style Transfer Extension

import spacy

nlp = spacy.load("en_core_web_sm")

def generate_prompts(text):
    doc = nlp(text)

    pos_strings = [token.text for token in doc if token.pos_ in ["ADJ", "NOUN", "VERB", "ADV", "PRON", "PROPN"]]
    
    cc_str = ' '.join(pos_strings)
    
    sentence_tokens = list(nlp(cc_str).sents)
    
    siz = len(sentence_tokens) // 10
    grouped_sentences = [sentence_tokens[i:i+siz] for i in range(0, len(sentence_tokens), siz)]
    
    groups = [' '.join([x.text for x in g]) for g in grouped_sentences]
    
    # Add prefix and suffix to each string
    prompts = ["Create this in an oil painting style.\n " + x + ".\nKeep a similar style for all the prompts (Same character designs and clothes and colors)." for x in groups]
    
    return prompts

# sample text that can be changed to any short story
sample_text = """
Hanuman was also applauded by Suras who showered flower petals
on him. The Sun God silently blessed Hanuman by radiating less of
heat. The wind God Vayu turned into a gentle breeze and wished his
son success.
To test Hanuman’s devotion towards Rama, the Devas sent Surasa,
who obstructed Hanuman’s flight. She turned herself into a
demoness and opened her mouth wide. Hanuman grew bigger in
size. She opened her mouth several miles wide and challenged
Hanuman that she would let him pass only if he could enter her
mouth. Hanuman at once shrunk his body to the size of thumb and
even before Surase could realize what was happening, got in and got
out of her mouth. Surase regained her earlier form and wished him
well.
Hanuman encounters several more obstacles but he overcame all of
them. He finally landed on Mount Trikuta on which the city of Lanka
had been set up.
Lanka city was dazzling city. It had beautiful gardens and parks. The
city was surrounded by forts; fierce looking Rakshas kept watch day
and night and never let any stranger enter the city. So Hanuman
decided to turn into a very tiny being and slip past the guards. Soon,
it was dark all over and Hanuman tried to climb over the fort wall
and enter Lanka. But he spotted by Lankini, the protector of Lanka
and she tried to stamp him with her massive feet. The enraged
Hanuman punched her very hard and with blood running out of her
nose and ears, Lankini slumped to the ground. He then quickly
entered the city.
Bearing in mind Rama’s description of Sita, Hanuman searched for
her all over Lanka. But everywhere he found only hideous looking
Rakshasas. He then peeped into each and every house but could not
find Sita. “Ravana might have forced her to stay in the royal
chamber. Let me cheek there” thought Hanuman but could not find
her there. He closely examined each wife of Ravana including
Mandodari but none could match the description of Sita. Hanuman
got worried. If he were to go back to Rama empty handed, Rama
34
would die. This would lead to Lakshmana’s death too. Unable to bear
the news, Bharatha, Shatrugna, Kaushalya ….. and the entire
Ayodhya will die mourning for Rama. Sugriva will end his life unable
to bear his friend Rama’s death. Hanuman trembled to think of the
consequences if he could not find Sita. “Whatever happens, I will not
return to Kishkinda unless I have news of Sita” swore Hanuman.
Searching for Sita, Hanuman entered the Ashoka garden. With
hundreds of trees, the garden looked beautiful. And under a tree sat
a beautiful lady. All her clothes were torn and faded. She looked
pale. The beautiful lady was surrounded by ugly looking Rakshasis
who kept on praising Ravana in front of her. By then, Hanuman
recalled seeing Sita when she threw down the ornaments. He felt
happy and relieved that Sita was alive. But at the same time he felt
sorry for her condition and also felt sad that a person like Sita had to
undergo such cruelty. Hanuman decided to talk to her when she was
alone. So he climbed the tree above her and hid himself amongst the
branches.
In a short while, Ravana reached the garden and tried his best to
make Sita like him. Hanuman was furious to hear such talk that he
wanted to kill Ravana at that very spot. Sita even refused to listen to
what Ravana was saying, and closing her ears said in a firm voice “I
belong to Rama totally. Rama will definitely come and rescue me.
That will be the final day of your life. Get out.” The irritated Ravana
ordered the Rakshasis to make Sita change her mind with the
exception of kind Rakshasi called Trijata; all the others pestered Sita
but in vain. Finally they gave up and went off to sleep. Unable to
bear the situation any longer, Sita decided to hang herself from the
tree and die.
Hanuman who was watching Sita said softly “Rama, Rama,” Sita
stopped and looked up. She saw a monkey. She thought that Ravana
was up to some magic tricks. Hanuman then talked about what
Rama liked and what he did not. Sita’s hand which was about to tie
the noose stopped. Hanuman slowly got down from the tree and
bowing his head before Sita, introduced himself as Rama’s humble
servant. To remove any doubts from her mind, Hanuman showed her
the ring sent by Rama. Tears of happiness filled up Sita’s eyes as
35
soon as she saw her husband’s ring. She could then believe
Hanuman when he told her that Rama would soon be waging a war
against Ravana and rescue her from Lanka. She gave Hanuman one
of her ornaments and blessed him “Please convey my love to Rama.
Let him kill Ravana and rescue me from here very soon. Let there be
no obstacles in your way. Be successful.
Now that Hanuman had met Sita, he decided that he would find out
about Ravenna’s army and his strength and inform Sugriva of them.
He had a plan. He provoked all the Rakshasas to attack him and
when they did, he jumped and trampled all the trees in Asoka
garden. The Rakshasas rushed to capture him but he killed them,
when Ravenna’s commander-in-chief and other able soldiers tried to
catch the monkey but were defeated and killed by the mighty
monkey. When Ravana heard about the destruction caused by a
monkey, he sent his son Indrajit to capture the monkey.
Indrajit was a very skilled warrior, who, at one time, had even
defeated Devendra. He used one of his powerful weapons on
Hanuman, imprisoned him and dragged him to Ravenna’s court.
When Hanuman was brought before the king, he was very impressed
with the ten-headed Ravana. His court was very grand and dazzling.
Ravana was sitting on a high throne. As soon as Hanuman came face
to face with Ravana, he freed himself from chains and ropes,
prepared a high seat out of his very long tail and sat on it.
“O Monkey! Who are you? And why did you destroy the Asoka
garden” asked Ravana.
“Sir” replied Hanuman “I am Rama’s messenger. I came to Lanka in
search of Sita. You have committed a great mistake by abducting
Sita. If you want to live, you return Sita to Rama gracefully and seek
refuge in him. Otherwise you are sure to die”.
Having warned Ravana thus, Hanuman added “Listen! I myself could
have rescued Sita from here and carry her on my shoulders. But I do
not have such orders. Only Rama should do this. And don’t
underestimate Rama. He is the lord of the entire universe. Don’t
seek your own destruction by angering him.”
36
Ravana was very angry “How dare a monkey talk to a king like me in
such a way” he thundered. He ordered his soldiers “Kill this arrogant
Vanara.” But Vibhishana, his brother, stopped him. “Brother, he is
after all Rama’s messenger. A king does not kill a messenger.
Instead, you can punish him suitably and let him suitably and let him
go back to Rama. He can tell Rama about strength and power.
“Yes brother” agreed Ravana “What you say makes sense.” He then
ordered his servants to set fire to Hanuman’s long tail and make him
walk in the streets of Lanka.
The Rakshasas dipped the monkey’s tail in oil and set fire to it.
Anjaneya used it as a whip and lashed all the Rakshasas. He then
jumped from building and reduced them to ashes, he did not even
spare Ravenna’s place. The whole of Lanka looked like an enormous
fire pit.
He only spared the Ashoka garden. He made sure that Sita was safe
and after seeking her blessings, left Lanka. He dipped his tail in the
sea water, expanded his body, climbed a nearby mountain and with
a powerful thrust, flew off.
Hanuman reached Kishkinda and told Rama all about Sita’s safety.
He conveyed her message also. He then handed over the ornament
Sita had sent as a momento.
Sugriva and the entire Vanara army felt proud that Hanuman was
able to accomplish his mission. Sugriva hugged Hanuman and
congratulated him.

"""

prompts = generate_prompts(sample_text)
i = 0
print("\n")
for prompt in prompts:
    i+=1
    print(i, prompt, "\n")
    
