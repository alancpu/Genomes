sample_snps = [
    {'title': 'Eye Color', 'rs_id':'rs12913832', 'dnaPair':'GG', 'outcome':'Makes your eyes blue', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/MjBZaed9yzM" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Eye Color', 'rs_id':'rs12913832', 'dnaPair':'AA', 'outcome':'Makes your eyes brown, or less likely blue', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/MjBZaed9yzM" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Eye Color', 'rs_id':'rs12913832', 'dnaPair':'AG', 'outcome':'Makes your eyes brown', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/MjBZaed9yzM" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Malaria Resistance', 'rs_id': 'rs8177374', 'dnaPair': 'CC', 'outcome': 'You have a normal resistance to Malaria', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/j9_Vq78Ljzc" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Malaria Resistance', 'rs_id': 'rs8177374', 'dnaPair': 'CT', 'outcome': 'You have a normal resistance to Malaria', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/j9_Vq78Ljzc" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Malaria Resistance', 'rs_id': 'rs8177374', 'dnaPair': 'TT', 'outcome': 'You have an increased resistance to Malaria and Tuberculosis', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/j9_Vq78Ljzc" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Alcohol Cravings', 'rs_id':'rs1799971', 'dnaPair':'AA', 'outcome':'You may experience normal cravings for alcoholic beverages', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/b7m6tIIi9WU" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Alcohol Cravings', 'rs_id':'rs1799971', 'dnaPair':'AG', 'outcome':'You may experience stronger cravings for alcoholic beverages', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/b7m6tIIi9WU" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Alcohol Cravings', 'rs_id':'rs1799971', 'dnaPair':'GG', 'outcome':'You may have heightened cravings for alcohol consumption', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/b7m6tIIi9WU" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Cannabis Affinity', 'rs_id':'rs806380', 'dnaPair':'AA', 'outcome':'You may have a high affinity for cannabis', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/nEQ6JTNIImA" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Cannabis Affinity', 'rs_id':'rs806380', 'dnaPair':'AG', 'outcome':'You might have a slightly lower affinity for cannabis', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/nEQ6JTNIImA" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Cannabis Affinity', 'rs_id':'rs806380', 'dnaPair':'GG', 'outcome':'You may potentially have a lower affinity for cannabis', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/nEQ6JTNIImA" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Novelty Seeking', 'rs_id':'rs1800955', 'dnaPair':'CC', 'outcome':'You have an increased susceptibility for your tendency to seek novelty', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/YDnXcgOzadk" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Novelty Seeking', 'rs_id':'rs1800955', 'dnaPair':'CT', 'outcome':'You have an increased susceptibility for your tendency to seek novelty', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/YDnXcgOzadk" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Novelty Seeking', 'rs_id':'rs1800955', 'dnaPair':'TT', 'outcome':'Your susceptibility for your tendency to seek novelty is normal', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/YDnXcgOzadk" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Empathetic Personality', 'rs_id': 'rs53576', 'dnaPair': 'AA', 'outcome': 'There are high chances that you may lack empathy', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/lu7ZtY0ectw" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Empathetic Personality', 'rs_id': 'rs53576', 'dnaPair': 'AG', 'outcome': 'There are high chances that you may lack empathy', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/lu7ZtY0ectw" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Empathetic Personality', 'rs_id': 'rs53576', 'dnaPair': 'GG', 'outcome': 'You are likely to be optimistic and empathetic', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/lu7ZtY0ectw" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Muscle performance', 'rs_id': 'rs1815739', 'dnaPair': 'CC', 'outcome': 'You have increased muscle performance', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/x3AsH_T52-k" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Muscle performance', 'rs_id': 'rs1815739', 'dnaPair': 'CT', 'outcome': 'You may have an increased likelihood of having better muscle performance', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/x3AsH_T52-k" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Muscle performance', 'rs_id': 'rs1815739', 'dnaPair': 'TT', 'outcome': 'You may be lacking in muscle performance, however, it could benefit endurance athletes', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/x3AsH_T52-k" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Risk of hair loss', 'rs_id': 'rs6152', 'dnaPair': 'AA', 'outcome': 'You have a low likelihood of going bald', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/N5plbx-i2Kw" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Risk of hair loss', 'rs_id': 'rs6152', 'dnaPair': 'AG', 'outcome': 'You have an increased risk of baldness', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/N5plbx-i2Kw" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Risk of hair loss', 'rs_id': 'rs6152', 'dnaPair': 'GG', 'outcome': 'You have a heightened risk of baldness', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/N5plbx-i2Kw" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'ADHD and Error avoidance', 'rs_id': 'rs1800497', 'dnaPair': 'CC', 'outcome': 'You are better at avoidance of errors, have normal risk for OCD, unlikely to have ADHD', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/3NlaekvCZ48" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'ADHD and Error avoidance', 'rs_id': 'rs1800497', 'dnaPair': 'CT', 'outcome': 'You may be bad at avoidance of errors, low risk for OCD, likely to have ADHD', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/3NlaekvCZ48" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'ADHD and Error avoidance', 'rs_id': 'rs1800497', 'dnaPair': 'TT', 'outcome': 'You may experience minimal pleasure response, increased pleasure seeking and/or addictive behavior, very likely to have ADHD', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/3NlaekvCZ48" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Diabetes and/or Obesity', 'rs_id': 'rs9939609', 'dnaPair': 'AA', 'outcome': 'You have an increased likelihood of diabetes, as well as obesity', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/XfyGv-xwjlI" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Diabetes and/or Obesity', 'rs_id': 'rs9939609', 'dnaPair': 'AT', 'outcome': 'You are at a normal risk for diabetes, but may potentially be at risk for obesity', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/XfyGv-xwjlI" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Diabetes and/or Obesity', 'rs_id': 'rs9939609', 'dnaPair': 'TT', 'outcome': 'You are at a minimal risk of diabetes and obesity', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/XfyGv-xwjlI" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Risk for early Heart Attack', 'rs_id': 'rs662799', 'dnaPair': 'AA', 'outcome': 'Your risk of weight gain and early heart attack is normal', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/83FYZ23h6lA" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Risk for early Heart Attack', 'rs_id': 'rs662799', 'dnaPair': 'AG', 'outcome': 'You may have an increased risk of early heart attack, but can be avoided with proper dieting', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/83FYZ23h6lA" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Risk for early Heart Attack', 'rs_id': 'rs662799', 'dnaPair': 'GG', 'outcome': 'You may experience a high likelihood of weight gain / early heart disease and/or early heart attack', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/83FYZ23h6lA" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Earwax and body odor', 'rs_id': 'rs17822931', 'dnaPair': 'CC', 'outcome': 'You may have wet earwax and should have normal body odor', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/99u02vOvNvg" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Earwax and body odor', 'rs_id': 'rs17822931', 'dnaPair': 'CT', 'outcome': 'You may have wet earwax but with better smelling body odor', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/99u02vOvNvg" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Earwax and body odor', 'rs_id': 'rs17822931', 'dnaPair': 'TT', 'outcome': 'You may have dry earwax, but no body odor', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/99u02vOvNvg" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Dopamine and stress', 'rs_id': 'rs4680', 'dnaPair': 'AA', 'outcome': 'You may experience more explatory behavior, increased dopamine levels but susceptible to stress', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/Z79QqrZrzV4" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Dopamine and stress', 'rs_id': 'rs4680', 'dnaPair': 'AG', 'outcome': 'You may experience normal explatory behavior, regular dopamine levels and stress response', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/Z79QqrZrzV4" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Dopamine and stress', 'rs_id': 'rs4680', 'dnaPair': 'GG', 'outcome': 'You may experience less explatory behavior, lower dopamine levels, increased response to stress', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/Z79QqrZrzV4" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Lactose Intolerance', 'rs_id': 'rs4988235', 'dnaPair': 'CC', 'outcome': 'You have a high likelihood of being lactose intolerant', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/oBwtxdI1zvk" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Lactose Intolerance', 'rs_id': 'rs4988235', 'dnaPair': 'CT', 'outcome': 'You may potentially be able to consume milk/lactose', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/oBwtxdI1zvk" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Lactose Intolerance', 'rs_id': 'rs4988235', 'dnaPair': 'TT', 'outcome': 'You can definitely consume milk/lactose without gastrointestinal distress', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/oBwtxdI1zvk" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Thrombosis (Blood clotting)', 'rs_id': 'rs6025', 'dnaPair': 'AA', 'outcome': 'You have a 9x increased risk for thrombosis', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/zyDkiubLZQs" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Thrombosis (Blood clotting)', 'rs_id': 'rs6025', 'dnaPair': 'AG', 'outcome': 'You have an increased likelihood for thrombosis', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/zyDkiubLZQs" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Thrombosis (Blood clotting)', 'rs_id': 'rs6025', 'dnaPair': 'GG', 'outcome': 'Your risk for thrombosis is normal', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/zyDkiubLZQs" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Rheumatoid Arthritis/ Lupus/ (T-1) Diabetes', 'rs_id': 'rs7574865', 'dnaPair': 'GG', 'outcome': 'Your risk for Rheumatoid Arthritis (RA), lupus, and/or Type-1 Diabetes is normal', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/8ycJt4lAlfQ" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Rheumatoid Arthritis/ Lupus/ (T-1) Diabetes', 'rs_id': 'rs7574865', 'dnaPair': 'GT', 'outcome': 'You have a 1.3x increased risk for Rheumatoid Arthritis (RA), lupus, and/or Type-1 Diabetes', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/8ycJt4lAlfQ" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Rheumatoid Arthritis/ Lupus/ (T-1) Diabetes', 'rs_id': 'rs7574865', 'dnaPair': 'TT', 'outcome': 'You have a 2.6x increased risk for Rheumatoid Arthritis (RA), lupus, and/or Type-1 Diabetes', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/8ycJt4lAlfQ" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Asthma', 'rs_id': 'rs1695', 'dnaPair': 'AA', 'outcome': 'You have a normal risk for asthma', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/7EDo9pUYvPE" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Asthma', 'rs_id': 'rs1695', 'dnaPair': 'AG', 'outcome': 'You have a normal risk for asthma', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/7EDo9pUYvPE" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Asthma', 'rs_id': 'rs1695', 'dnaPair': 'GG', 'outcome': 'You have a high likelihood of having asthma related symptoms', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/7EDo9pUYvPE" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Cilantro', 'rs_id': 'rs72921001', 'dnaPair': 'AA', 'outcome': 'You are least likely to dislike cilantro, should not taste like soap', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/6ymoPRWxZl8" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Cilantro', 'rs_id': 'rs72921001', 'dnaPair': 'AC', 'outcome': 'You are less likely to dislike cilantro, may potentially taste like soap', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/6ymoPRWxZl8" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Cilantro', 'rs_id': 'rs72921001', 'dnaPair': 'CC', 'outcome': 'You may have an increased likelihood of disliking cilantro', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/6ymoPRWxZl8" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Periodontitis (Gum inflammatory disease)', 'rs_id': 'rs1537415', 'dnaPair': 'CC', 'outcome': 'Your likelihood of developing periodontitis is normal', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/nk9bNV-_TbM" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Periodontitis (Gum inflammatory disease)', 'rs_id': 'rs1537415', 'dnaPair': 'CG', 'outcome': 'You have a 1.6x increased risk of developing periodontitis', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/nk9bNV-_TbM" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Periodontitis (Gum inflammatory disease)', 'rs_id': 'rs1537415', 'dnaPair': 'GG', 'outcome': 'You have a 2x increased risk of developing periodontitis', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/nk9bNV-_TbM" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Coffee Affinity', 'rs_id': 'rs2472297', 'dnaPair': 'CC', 'outcome': 'You have a normal affinity for drinking coffee', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/4YOwEqGykDM" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Coffee Affinity', 'rs_id': 'rs2472297', 'dnaPair': 'CT', 'outcome': 'You have an increased affinity for drinking coffee', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/4YOwEqGykDM" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Coffee Affinity', 'rs_id': 'rs2472297', 'dnaPair': 'TT', 'outcome': 'You have an increased affinity for drinking coffee', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/4YOwEqGykDM" frameborder="0" allowfullscreen></iframe>'},

    {'title': 'Warrior Gene (Behavioral Aggression)', 'rs_id': 'rs909525', 'dnaPair': 'AA', 'outcome': 'No warrior gene is present in your DNA', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/jRIOgdz_AIM" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Warrior Gene (Behavioral Aggression)', 'rs_id': 'rs909525', 'dnaPair': 'AG', 'outcome': 'You have a normal potential of having the warrior gene', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/jRIOgdz_AIM" frameborder="0" allowfullscreen></iframe>'},
    {'title': 'Warrior Gene (Behavioral Aggression)', 'rs_id': 'rs909525', 'dnaPair': 'GG', 'outcome': 'You have a high likelihood of having the warrior gene', 'video': '<iframe width="420" height="315" src="https://www.youtube.com/embed/jRIOgdz_AIM" frameborder="0" allowfullscreen></iframe>'}
]
