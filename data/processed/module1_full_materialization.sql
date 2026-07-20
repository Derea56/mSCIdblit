-- Module 1 full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m1_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m1_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m1_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m1_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m1_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m1_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Histological repair of damaged spinal cord tissue from chronic contusion injury of rat: a LM observation', 'Shu-xin Zhang; Fengfa Huang; Mary Gates; Jason White; Eric G Holmberg', 2011,
    'Histology and Histopathology', '26', '1',
    '45-58', '10.14670/HH-26.45', '21117026',
    'https://pubmed.ncbi.nlm.nih.gov/21117026/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury', 'Tetsuya Tamaru; Kazu Kobayakawa; Hirokazu Saiwai; Daijiro Konno; Ken Kijima; Shingo Yoshizaki; Kazuhiro Hata; Hirotaka Iura; Gentaro Ono; Yohei Haruta; Kazuki Kitade; Kei-Ichiro Iida; Ken-Ichi Kawaguchi; Yoshihiro Matsumoto; Kensuke Kubota; Takeshi Maeda; Seiji Okada; Yasuharu Nakashima', 2023,
    'Experimental Neurology', '359', NULL,
    '114264', '10.1016/j.expneurol.2022.114264', '36336030',
    'https://catalog.lib.kyushu-u.ac.jp/opac_download_md/6787512/med3703.pdf'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Spatiotemporal Dynamics of the Molecular Expression Pattern and Intercellular Interactions in the Glial Scar Response to Spinal Cord Injury', 'Leilei Gong; Yun Gu; Xiaoxiao Han; Chengcheng Luan; Chang Liu; Xinghui Wang; Yufeng Sun; Mengru Zheng; Mengya Fang; Shuhai Yang; Lai Xu; Hualin Sun; Bin Yu; Xiaosong Gu; Songlin Zhou', 2023,
    'Neuroscience Bulletin', '39', '2',
    '213-244', '10.1007/s12264-022-00897-8', '35788904',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC9905408/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Resection of glial scar following spinal cord injury', 'Alexandre Rasouli; Nitin Bhatia; Paul Dinh; Kim Cahill; Sourabh Suryadevara; Ranjan Gupta', 2009,
    'Journal of Orthopaedic Research', '27', '7',
    '931-936', '10.1002/jor.20793', '19062171',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC2696557/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice', 'Yun Li; Rodney M Ritzel; Niaz Khan; Tuoxin Cao; Junyun He; Zhuofan Lei; Jessica J Matyas; Boris Sabirzhanov; Jiping Wang', 2020,
    'Theranostics', '10', '25',
    '11376-11403', '10.7150/thno.49199', '33052221',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC7545988/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Fibronectin EDA forms the chronic fibrotic scar after contusive spinal cord injury', 'John G. Cooper; Su Ji Jeong; Tammy L. McGuire; Sripadh Sharma; Wenxia Wang; Swati Bhattacharyya; John Varga; John A. Kessler', 2018,
    'Neurobiology of Disease', '116', NULL,
    '60-68', '10.1016/j.nbd.2018.04.014', '29705186',
    'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5995671/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Perivascular Fibroblasts Form the Fibrotic Scar after Contusive Spinal Cord Injury', 'Cynthia Soderblom; Xueting Luo; Ezra Blumenthal; Eric Bray; Kirill Lyapichev; Jose Ramos; Vidhya Krishnan; Catherine Lai-Hsu; Kevin K Park; Pantelis Tsoulfas; Jae K Lee', 2013,
    'The Journal of Neuroscience', '33', '34',
    '13882-13887', '10.1523/JNEUROSCI.2524-13.2013', '23966707',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC3755723/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury', 'David Oliveira Dias; Hoseok Kim; Daniel Holl; Beata Werne Solnestam; Joakim Lundeberg; Marie Carlen; Christian Goritz; Jonas Frisen', 2018,
    'Cell', '173', '1',
    '153-165.e22', '10.1016/j.cell.2018.02.004', '29502968',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC5871719/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Collagen scaffold combined with human umbilical cord-derived mesenchymal stem cells promote functional recovery after scar resection in rats with chronic spinal cord injury', 'Nuo Wang; Zhifeng Xiao; Yannan Zhao; Bin Wang; Xing Li; Jing Li; Jianwu Dai', 2018,
    'Journal of Tissue Engineering and Regenerative Medicine', '12', '2',
    'e1154-e1163', '10.1002/term.2450', '28482124',
    'https://pubmed.ncbi.nlm.nih.gov/28482124/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Chronic alterations in the cellular composition of spinal cord white matter following contusion injury', 'Lisa J Rosenberg; Laila J Zai; Jean R Wrathall', 2005,
    'Glia', '49', '1',
    '107-120', '10.1002/glia.20096', '15390101',
    'https://pubmed.ncbi.nlm.nih.gov/15390101/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Lesion-remote astrocytes govern microglia-mediated white matter repair', 'Sarah McCallum; Keshav B Suresh; Timothy S Islam; Manish K Tripathi; Ann W Saustad; Oksana Shelest; Aditya Patil; David Lee; Brandon Kwon; Katherine Leitholf; Inga Yenokian; Sophia E Shaka; Connor H Beveridge; Palak Manchandra; Caitlin E Randolph; Gordon P Meares; Ranjan Dutta; Jasmine Plummer; Vinicius F Calsavara; Riki Kawaguchi; Simon R V Knott; Gaurav Chopra; Joshua E Burda', 2026,
    'Nature', '649', '8098',
    '959-970', '10.1038/s41586-025-09887-y', '41407858',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC12823418/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Longitudinal motor system changes from acute to chronic spinal cord injury', 'Tim M Emmenegger; Dario Pfyffer; Armin Curt; Simon Schading-Sassenhausen; Markus Hupp; John Ashburner; Karl Friston; Nikolaus Weiskopf; Patrick Freund', 2024,
    'European Journal of Neurology', '31', '4',
    'e16196', '10.1111/ene.16196', '38258488',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC11235629/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Human spinal cord retains substantial structural mass in chronic stages after injury', 'Mark H Tuszynski; Katie Gabriel; Kevin Gerhardt; Suzanne Szollar', 1999,
    'Journal of Neurotrauma', '16', '6',
    '523-531', NULL, '10391368',
    'https://pubmed.ncbi.nlm.nih.gov/10391368/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Motoneuron Death after Human Spinal Cord Injury', 'Robert M Grumbles; Christine K Thomas', 2017,
    'Journal of Neurotrauma', '34', '3',
    '581-590', '10.1089/neu.2015.4374', '27349409',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC5286554/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Vascular mechanisms in the pathophysiology of human spinal cord injury', 'Charles H Tator; Izumi Koyanagi', 1997,
    'Journal of Neurosurgery', '86', '3',
    '483-492', '10.3171/jns.1997.86.3.0483', NULL,
    'https://thejns.org/view/journals/j-neurosurg/86/3/article-p483.xml'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Heterogeneous fibroblasts contribute to fibrotic scar formation after spinal cord injury in mice and monkeys', 'Xiaoyu Xue; Xianming Wu; Yongheng Fan; Shuyu Han; Haipeng Zhang; Yuting Sun; Yanyun Yin; Man Yin; Bing Chen; Zheng Sun; Shuaijing Zhao; Qi Zhang; Weiyuan Liu; Jiaojiao Zhang; Jiayin Li; Ya Shi; Zhifeng Xiao; Jianwu Dai; Yannan Zhao', 2024,
    'Nature Communications', '15', '1',
    '6321', '10.1038/s41467-024-50564-x', '39060269',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC11282111/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'One-year clinical study of NeuroRegen scaffold implantation following scar resection in complete chronic spinal cord injury patients', 'Zhifeng Xiao; Fengwu Tang; Jiaguang Tang; Huilin Yang; Yannan Zhao; Bing Chen; Sufang Han; Nuo Wang; Xing Li; Shixiang Cheng; Guang Han; Changyu Zhao; Xiaoxiong Yang; Yumei Chen; Qin Shi; Shuxun Hou; Sai Zhang; Jianwu Dai', 2016,
    'Science China Life Sciences', '59', '7',
    '647-655', '10.1007/s11427-016-5080-z', '27333785',
    'https://link.springer.com/article/10.1007/s11427-016-5080-z'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Post-mortem assessment of rat spinal cord injury and white matter sparing using inversion recovery-supported proton density magnetic resonance imaging', 'F Scholtes; E Theunissen; R Phan-Ba; P Adriaensens; G Brook; R Franzen; J Gelan; J Schoenen; D Martin', 2011,
    'Spinal Cord', '49', '3',
    '345-351', '10.1038/sc.2010.129', '20877332',
    'https://www.nature.com/articles/sc2010129'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Softening of the chronic hemi-section spinal cord injury scar parallels dysregulation of cellular and extracellular matrix content', 'Hannah J Baumann; Gautam Mahajan; Trevor R Ham; Patricia Betonio; Chandrasekhar R Kothapalli; Leah P Shriver; Nicholas D Leipzig', 2020,
    'Journal of the Mechanical Behavior of Biomedical Materials', '110', NULL,
    '103953', '10.1016/j.jmbbm.2020.103953', '32957245',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC7509206/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P026', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Spinal Cord Injury Results in Chronic Mechanical Stiffening', 'John G Cooper; Delphine Sicard; Sripadh Sharma; Stephanie Van Gulden; Tammy L McGuire; Miguel Pareja Cajiao; Daniel J Tschumperlin; John A Kessler', 2020,
    'Journal of Neurotrauma', '37', '14',
    '1568-1581', '10.1089/neu.2019.6540', '31516087',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC6978780/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P027', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'DTI of chronic spinal cord injury in children without MRI abnormalities and with pathology on MRI and comparison to severity of motor impairment', 'Scott H Faro; Sona Saksena; Laura Krisa; Devon M Middleton; Mahdi Alizadeh; Jurgen Finsterbusch; Adam E Flanders; Kiran Talekar; M J Mulcahey; Feroze B Mohamed', 2022,
    'Spinal Cord', '60', '5',
    '457-464', '10.1038/s41393-022-00770-5', '35379960',
    'https://www.nature.com/articles/s41393-022-00770-5'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P028', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Microglia and macrophages promote corralling, wound compaction and recovery after spinal cord injury via Plexin-B2', 'Xiang Zhou; Shalaka Wahane; Marie-Sophie Friedl; Michael Kluge; Caroline C Friedel; Kleopatra Avrampou; Venetia Zachariou; Lei Guo', 2020,
    'Nature Neuroscience', '23', '3',
    '337-350', '10.1038/s41593-020-0597-7', '32112058',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC7412870/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P030', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Single-cell analysis of the cellular heterogeneity and interactions in the injured mouse spinal cord', 'Lindsay M Milich; James S Choi; Christine Ryan; Susana R Cerqueira; Sofia Benavides; Stephanie L Yahn; Pantelis Tsoulfas; Jae K Lee', 2021,
    'Journal of Experimental Medicine', '218', '8',
    NULL, '10.1084/jem.20210040', '34132743',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC8212781/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P031', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Astrocytic Ryk signaling coordinates scarring and wound healing after spinal cord injury', 'Zhe Shen; Bo Feng; Wei Ling Lim; Timothy Woo; Yanlin Liu; Silvia Vicenzi; Jingyi Wang; Brian K Kwon', 2025,
    'Proceedings of the National Academy of Sciences of the United States of America', '122', '15',
    'e2417400122', '10.1073/pnas.2417400122', '40208942',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC12012454/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P032', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Derivation and transcriptional reprogramming of border-forming wound repair astrocytes after spinal cord injury or stroke in mice', 'Timothy M O''Shea; Yan Ao; Shinong Wang; Yilong Ren; Amy L Cheng; Riki Kawaguchi; Zechuan Shi; Vivek Swarup', 2024,
    'Nature Neuroscience', '27', '8',
    '1505-1521', '10.1038/s41593-024-01684-6', '38907165',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC11303254/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P033', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Histological effects of combined therapy involving scar resection, decellularized scaffolds, and human iPSC-NS/PCs transplantation in chronic complete spinal cord injury', 'Keitaro Ito; Munehisa Shinozaki; Shogo Hashimoto; Yusuke Saijo; Yu Suematsu; Tomoharu Tanaka; Kotaro Nishi; Hiroshi Yagi', 2024,
    'Scientific Reports', '14', '1',
    '31500', '10.1038/s41598-024-82959-7', '39733145',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC11682313/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P034', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'CSF1R Inhibition Reduces Microglia Proliferation, Promotes Tissue Preservation and Improves Motor Recovery After Spinal Cord Injury', 'Yannick Nicolas Gerber; Guillaume Patrick Saint-Martin; Claire Mathilde Bringuier; Sylvain Bartolami; Christophe Goze-Bac; Harun Najib Noristani; Florence Evelyne Perrin', 2018,
    'Frontiers in Cellular Neuroscience', '12', NULL,
    '368', '10.3389/fncel.2018.00368', '30386212',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC6198221/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P035', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)
  VALUES (
    'Testing Pathological Variation of White Matter Tract in Adult Rats after Severe Spinal Cord Injury with MRI', 'Wei Song; Guiyun Song; Can Zhao; Xiaoguang Li; Xiaojiao Pei; Wen Zhao; Yudan Gao; Jia-Sheng Rao', 2018,
    'BioMed Research International', '2018', NULL,
    '4068156', '10.1155/2018/4068156', '30534561',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC6252222/'
  )
  RETURNING paper_id
)
INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT 'M1A-P036', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P001',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P003',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P004',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P005',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P006',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P007',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P008',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P009',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P012',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P013',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P014',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P016',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P018',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P019',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P020',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P021',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P022',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P024',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P026',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P026'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P026', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P027',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P027'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P027', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P028',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P028'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P028', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P030',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P030'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P030', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P031',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P031'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P031', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P032',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P032'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P032', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P033',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P033'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P033', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P034',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P034'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P034', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P035',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P035'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P035', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 1 curated evidence extraction',
    'First-pass Module 1 lesion-architecture curation for M1A-P036',
    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'
  FROM _m1_paper_map WHERE tracker_id = 'M1A-P036'
  RETURNING paradigm_id
)
INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT 'M1A-P036', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P001-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O045"], "tracker_id": "M1A-P001-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P001'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P001-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P003-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O027"], "tracker_id": "M1A-P003-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P003-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O028"], "tracker_id": "M1A-P003-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P003-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P003-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O029"], "tracker_id": "M1A-P003-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P003-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P003-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O030"], "tracker_id": "M1A-P003-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P003-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    5,
    'Tracker experiment M1A-P003-E005',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O085"], "tracker_id": "M1A-P003-E005"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P003-E005', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    5,
    'Tracker experiment M1A-P003-E005–E006',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O031"], "tracker_id": "M1A-P003-E005\u2013E006"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P003-E005–E006', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    6,
    'Tracker experiment M1A-P003-E006',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O086"], "tracker_id": "M1A-P003-E006"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P003-E006', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P004-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O037"], "tracker_id": "M1A-P004-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P004'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P004-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O038"], "tracker_id": "M1A-P004-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P004'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P004-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P004-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O087"], "tracker_id": "M1A-P004-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P004'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P004-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P004-E003–E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O040"], "tracker_id": "M1A-P004-E003\u2013E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P004'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P004-E003–E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P004-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O039"], "tracker_id": "M1A-P004-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P004'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P004-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P005-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O056"], "tracker_id": "M1A-P005-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P005'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P005-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O057"], "tracker_id": "M1A-P005-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P005'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P005-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P006-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O071"], "tracker_id": "M1A-P006-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P006'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P006-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O072"], "tracker_id": "M1A-P006-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P006'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P006-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P006-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O073"], "tracker_id": "M1A-P006-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P006'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P006-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P006-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O075"], "tracker_id": "M1A-P006-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P006'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P006-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P006-E004–E005',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O076"], "tracker_id": "M1A-P006-E004\u2013E005"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P006'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P006-E004–E005', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    5,
    'Tracker experiment M1A-P006-E005',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O074"], "tracker_id": "M1A-P006-E005"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P006'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P006-E005', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P007-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O041"], "tracker_id": "M1A-P007-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P007'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P007-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O042"], "tracker_id": "M1A-P007-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P007'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P007-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P007-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O043"], "tracker_id": "M1A-P007-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P007'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P007-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P007-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O088"], "tracker_id": "M1A-P007-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P007'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P007-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P007-E004–E005',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O044"], "tracker_id": "M1A-P007-E004\u2013E005"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P007'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P007-E004–E005', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    5,
    'Tracker experiment M1A-P007-E005',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O089"], "tracker_id": "M1A-P007-E005"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P007'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P007-E005', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P008-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O012"], "tracker_id": "M1A-P008-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P008'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P008-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O013"], "tracker_id": "M1A-P008-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P008'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P008-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P008-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O014"], "tracker_id": "M1A-P008-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P008'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P008-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P008-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O015"], "tracker_id": "M1A-P008-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P008'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P008-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    5,
    'Tracker experiment M1A-P008-E005',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O016"], "tracker_id": "M1A-P008-E005"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P008'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P008-E005', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P009-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O017", "M1B-O018"], "tracker_id": "M1A-P009-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P009'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P009-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O019"], "tracker_id": "M1A-P009-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P009'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P009-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P009-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O020"], "tracker_id": "M1A-P009-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P009'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P009-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P009-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O021"], "tracker_id": "M1A-P009-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P009'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P009-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P012-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O058"], "tracker_id": "M1A-P012-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P012'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P012-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P013-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O055"], "tracker_id": "M1A-P013-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P013'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P013-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P014-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O047"], "tracker_id": "M1A-P014-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P014'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P014-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O048"], "tracker_id": "M1A-P014-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P014'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P014-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P014-E002–E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O049"], "tracker_id": "M1A-P014-E002\u2013E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P014'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P014-E002–E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P014-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O050"], "tracker_id": "M1A-P014-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P014'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P014-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P014-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O051"], "tracker_id": "M1A-P014-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P014'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P014-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    5,
    'Tracker experiment M1A-P014-E005',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O052"], "tracker_id": "M1A-P014-E005"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P014'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P014-E005', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P016-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O063"], "tracker_id": "M1A-P016-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P016'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P016-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O064"], "tracker_id": "M1A-P016-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P016'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P016-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P016-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O065"], "tracker_id": "M1A-P016-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P016'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P016-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P018-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O080"], "tracker_id": "M1A-P018-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P018'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P018-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O081"], "tracker_id": "M1A-P018-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P018'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P018-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P019-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O090"], "tracker_id": "M1A-P019-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P019'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P019-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O066"], "tracker_id": "M1A-P019-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P019'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P019-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P019-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O091"], "tracker_id": "M1A-P019-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P019'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P019-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P019-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O067"], "tracker_id": "M1A-P019-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P019'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P019-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P020-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O082"], "tracker_id": "M1A-P020-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P020'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P020-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O083"], "tracker_id": "M1A-P020-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P020'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P020-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P020-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O084"], "tracker_id": "M1A-P020-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P020'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P020-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P021-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O022"], "tracker_id": "M1A-P021-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P021'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P021-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O023"], "tracker_id": "M1A-P021-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P021'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P021-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P021-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O024"], "tracker_id": "M1A-P021-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P021'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P021-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P021-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O025"], "tracker_id": "M1A-P021-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P021'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P021-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    5,
    'Tracker experiment M1A-P021-E005',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O026"], "tracker_id": "M1A-P021-E005"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P021'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P021-E005', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P022-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O059"], "tracker_id": "M1A-P022-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P022'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P022-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O060", "M1B-O070"], "tracker_id": "M1A-P022-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P022'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P022-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P022-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O061"], "tracker_id": "M1A-P022-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P022'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P022-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P024-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O092"], "tracker_id": "M1A-P024-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P024'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P024-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P024-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O053"], "tracker_id": "M1A-P024-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P024'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P024-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P024-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O093"], "tracker_id": "M1A-P024-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P024'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P024-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P026-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O001"], "tracker_id": "M1A-P026-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P026'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P026-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P026-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O002"], "tracker_id": "M1A-P026-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P026'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P026-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P026-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O003"], "tracker_id": "M1A-P026-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P026'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P026-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P026-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O004", "M1B-O005"], "tracker_id": "M1A-P026-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P026'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P026-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P027-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O006"], "tracker_id": "M1A-P027-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P027'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P027-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P027-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O007"], "tracker_id": "M1A-P027-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P027'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P027-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    3,
    'Tracker experiment M1A-P027-E003',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O008"], "tracker_id": "M1A-P027-E003"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P027'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P027-E003', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    4,
    'Tracker experiment M1A-P027-E004',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O009", "M1B-O010", "M1B-O011"], "tracker_id": "M1A-P027-E004"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P027'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P027-E004', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P028-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O068"], "tracker_id": "M1A-P028-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P028'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P028-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P028-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O069"], "tracker_id": "M1A-P028-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P028'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P028-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P030-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O032"], "tracker_id": "M1A-P030-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P030'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P030-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P030-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O077"], "tracker_id": "M1A-P030-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P030'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P030-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P030-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O033"], "tracker_id": "M1A-P030-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P030'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P030-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P031-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O046", "M1B-O078"], "tracker_id": "M1A-P031-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P031'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P031-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P032-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O034"], "tracker_id": "M1A-P032-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P032'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P032-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P033-E001',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O035"], "tracker_id": "M1A-P033-E001"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P033'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P033-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tracker experiment M1A-P033-E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O036"], "tracker_id": "M1A-P033-E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P033'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P033-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P034-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O062"], "tracker_id": "M1A-P034-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P034'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P034-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P035-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O079"], "tracker_id": "M1A-P035-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P035'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P035-E001–E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Tracker experiment M1A-P036-E001–E002',
    'Module 1 tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M1B-O054"], "tracker_id": "M1A-P036-E001\u2013E002"}'
  FROM _m1_paper_map p
  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M1A-P036'
  RETURNING experiment_id
)
INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT 'M1A-P036-E001–E002', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('3D debris reconstruction / behavior', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('A-layer experiment evidence', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('AFM microindentation', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Association modeling', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Astrocyte signaling perturbation', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Astrocyte transplantation / LMD-qPCR', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Axon staining / behavior', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Axon tracing / IHC', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Behavioral / electrophysiology / histology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Behavioral assay / BDA tract tracing', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Behavioral assays / correlation', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Behavioral testing', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Biochemical ECM assay', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('CSF1R inhibition / recovery', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Cell culture morphology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Clinical safety / electrophysiology follow-up', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Comparative histology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Conditional deletion / histology / function', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('DOC/SDS fractionation', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Flow cytometry', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Flow cytometry / ROS / qPCR', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Genetic attenuation / histology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Histology / LMD-qPCR', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Histology / cellular composition', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Histology / morphometry', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Histology / stereology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Histology / transplantation', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human autopsy histopathology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human clinical surgery', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human post-mortem pathology / g-ratio', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human post-mortem pathology / ventral-root axon counts', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human scar tissue immunohistochemistry', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('IHC / western blot', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Image analysis / GFAP alignment', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Immunohistochemistry', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Immunophenotyping', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('In vitro antibody blockade', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('In vitro astrocyte culture', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('In vivo MRI / pathology-function linkage', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('In vivo antibody treatment', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('LSFM / immunophenotyping', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Light microscopy histology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Lineage analysis', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Longitudinal T2 MRI / clinical follow-up', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('MRI stereology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Monkey scRNA/snRNA-seq / IHC', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Myelin damage models / human tissue comparison', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Myeloid nuclear RNA-seq', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Myeloid transcriptomics / conditional deletion', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('NG2-CreER lineage tracing', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('NanoString / qPCR', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('NanoString / qPCR / brain stereology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Optogenetics / electrophysiology', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('PDGFRbeta lineage tracing / IHC', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Pathway analysis / in vitro assays', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Pediatric spinal cord DTI', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Pediatric spinal cord DTI / clinical severity', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Post-mortem MRI / histology / BBB', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Primary microglia / lipid assays', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Quantitative MRI / voxel-based mapping', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('RNA-seq / ECM validation', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('RNAscope / histology / conditional deletion', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('RiboTag / RNA-seq / snRNA-seq / spatial transcriptomics', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('ST reclustering / marker mapping', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Silicone rubber microangiography', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Spatial marker mapping', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Spatial transcriptomics / H&E', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Spatial transcriptomics / NMF', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Time-course IHC / LSFM', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Tissue transparency / ST marker maps', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('WGCNA / phase synthesis', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('qPCR / western blot', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('scRNA-seq / interaction inference', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('scRNA-seq / lineage tracing', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('snRNA-seq / temporal transcriptomics', 'Module 1 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('20 um mid-sagittal sections stained for SMI-312; axonal staining intensity quantified across distances from lesion center and normalized to 2 mm rostral tissue.', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('AIS-linked perilesional abnormality', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Acute intraspinal inflammation', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Acute vascular lesion pattern', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('After EGFP-positive Col-I-SA transplantation, anti-beta1 integrin antibody was injected at the transplant site; host EGFP-negative/GFAP-positive/N-cadherin-positive astrocyte recruitment was quantified.', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Anti-beta1 integrin antibody was injected into the spinal cord epicenter every 2 days from 14-26 DPI; GFAP/N-cadherin-positive chronic astrocytes and GAP43-positive area were quantified.', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Astrocyte mechanosensitivity', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon density and recovery', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axonal regeneration', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Baseline scar-lineage identity', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Blinded open-field locomotor scoring using BMS and modified BBB; mice with combined 24 h BMS >1 excluded as improperly injured.', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Border astrocyte origin', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Border morphology / wound architecture', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('CCN1 spatial regulation', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cell marker distribution', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic astrocytic scar persistence', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic cavitation and remote infarction', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic fibrotic scar anatomy', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic repaired-tissue zones', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic residual white matter cellularity', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic scar marker profile', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic scar modulation / axon growth', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic spinal cord inflammation', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Circuit integration', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Conserved white matter astrocyte state', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Corralling and containment', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cross-species conservation', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Debris clearance and recovery', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Fibroblast subtype function', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Fibroblast subtype organization', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Fibrosis program', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Fibrotic ECM isoform time course', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Fibrotic scar occupancy', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Fibrotic scar organization', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Five excised rat spines were imaged post-mortem using high-resolution proton density MRI with inversion recovery to depict lesion volume, cord atrophy, and spared white matter.', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Focal cystic atrophy', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Functional recovery', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Glial fiber alignment', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Human cord vascular supply', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Human ventral roots and cord sections were classified by lesion level and injury type; solochrome cyanine/Sevier-Munger cord pathology and toluidine blue ventral-root histology established tissue context and sampling.', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Hyaluronic acid content', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Imaging-recovery linkage', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Immune-glial scar ecology', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Injury-activated myeloid state', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Injury-induced marker shift', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Injury-model recruitment', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Injury-model scar geometry', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Large-diameter myelinated axons (>=7 um) were sampled and counted in ventral roots above, at, and below the lesion epicenter to estimate motoneuron loss relative to uninjured controls.', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Lesion and remote neurodegeneration', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Lesion geometry', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Lesion subregion stiffness', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Lesion-remote astrocyte states', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Matrix stability', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Method validation', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Microglia/macrophage modulation', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Microglial lipid handling', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Motoneuron loss', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Neurological recovery', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Normal-appearing cord abnormality', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Pathway robustness', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Pericyte contribution', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Post-injury myeloid response', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Preserved adjacent cord mass', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Remote brain inflammation', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Remote motor-system degeneration', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Remyelination abnormality', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Resected human scar composition', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Resection outcome after contusion', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Resection outcome after hemisection', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Safety and signal recovery', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scaffold-cell repair after chronic resection', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scaffold-supported cavitary repair', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar boundary mapping and gap filling', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar boundary markers', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar maturation phase model', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar spatial atlas', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar-cell source', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar-forming astrocyte recruitment', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar-forming astrocyte stability', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar-resident cell composition', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Single-cell lesion ecology', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Spared white matter imaging', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Sulfated GAG / CSPG content', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Tissue architecture', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('WGCNA and co-expression module analyses identified time-correlated scar modules, including ECM-receptor and lysosome-associated modules.', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Weekly BBB locomotor recovery was compared with MRI lesion severity and white matter sparing, and histology was used to confirm MRI interpretation.', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('White matter repair niche', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('White matter tract pathology', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Wound-repair astrocyte state', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Young''s modulus', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Young''s modulus after treatment', 'Module 1 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chronic rat hemisection scar/injury region had lower Young''s modulus than naive tissue; uninjured region averaged about 2.6-fold higher than around injury.',
    'Pa / fold-change',
    'Chronic rat hemisection scar/injury region had lower Young''s modulus than naive tissue; uninjured region averaged about 2.6-fold higher than around injury.',
    'scar softening vs naive tissue',
    'Results / Figure 1',
    'Fig 1',
    'high',
    '{"curator_notes": "Fresh 500 um sections, 80 um bead, right lateral hemisection, 15-18 WPI; source quote: \"2.6-fold higher\".", "paper_tracker_id": "M1A-P026", "quantitative": "YES", "statistics_reported": "p < 0.0001; Mann-Whitney-Wilcoxon; N = 3 independent tissues for Fig 1 summary", "topic_id": "M1B-T004", "tracker_id": "M1B-O001"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P026-E001'
    AND et.evidence_type_name = 'AFM microindentation'
    AND ot.outcome_type_name = 'Young''s modulus'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chronic hemisection scar contained cavitation/syrinx areas interspersed with dense, disorganized nuclei packing.',
    'qualitative + distance',
    'Chronic hemisection scar contained cavitation/syrinx areas interspersed with dense, disorganized nuclei packing.',
    'cavitary scar architecture with dense nuclei regions',
    'Results / Figure 2',
    'Fig 2',
    'high',
    '{"curator_notes": "Supports structural explanation for altered mechanics; source quote: \"areas of cavitation\".", "paper_tracker_id": "M1A-P026", "quantitative": "YES", "statistics_reported": "DNA content decreased; nuclei spacing quantified in source", "topic_id": "M1B-T004", "tracker_id": "M1B-O002"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P026-E002'
    AND et.evidence_type_name = 'Histology / morphometry'
    AND ot.outcome_type_name = 'Tissue architecture'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Scar tissue showed loss/dysregulation of dominant CNS cell markers with vimentin upregulation.',
    'normalized intensity',
    'Scar tissue showed loss/dysregulation of dominant CNS cell markers with vimentin upregulation.',
    'reduced CNS cell marker profile; increased vimentin',
    'Results / Figure 3',
    'Fig 3',
    'high',
    '{"curator_notes": "Markers included beta-III tubulin, GFAP, myelin/antigalactocerebroside, tenascin R, vimentin, and Hoechst.", "paper_tracker_id": "M1A-P026", "quantitative": "YES", "statistics_reported": "IHC quantified by normalized intensity", "topic_id": "M1B-T004", "tracker_id": "M1B-O003"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P026-E003'
    AND et.evidence_type_name = 'Immunohistochemistry'
    AND ot.outcome_type_name = 'Cell marker distribution'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Total sGAGs decreased in scar-containing tissue, while targeted CSPG analysis showed roughly two-fold increase versus naive tissue.',
    'relative quantity / fold-change',
    'Total sGAGs decreased in scar-containing tissue, while targeted CSPG analysis showed roughly two-fold increase versus naive tissue.',
    'total sGAG down; CSPG subset up',
    'Results / Figure 4',
    'Fig 4B-C',
    'high',
    '{"curator_notes": "Shows ECM components diverge by GAG subclass; source quote: \"nearly a two-fold increase\".", "paper_tracker_id": "M1A-P026", "quantitative": "YES", "statistics_reported": "Kruskal-Wallis with Dunn''s multiple comparison", "topic_id": "M1B-T004", "tracker_id": "M1B-O004"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P026-E004'
    AND et.evidence_type_name = 'Biochemical ECM assay'
    AND ot.outcome_type_name = 'Sulfated GAG / CSPG content'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Hyaluronic acid was upregulated in chronic scar tissue.',
    'concentration / relative quantity',
    'Hyaluronic acid was upregulated in chronic scar tissue.',
    'HA upregulated in chronic scar',
    'Results / Figure 4',
    'Fig 4D',
    'high',
    '{"curator_notes": "Authors interpret GAG/HA dysregulation as likely relevant to elastic behavior.", "paper_tracker_id": "M1A-P026", "quantitative": "YES", "statistics_reported": "Kruskal-Wallis with Dunn''s multiple comparison", "topic_id": "M1B-T004", "tracker_id": "M1B-O005"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P026-E004'
    AND et.evidence_type_name = 'Biochemical ECM assay'
    AND ot.outcome_type_name = 'Hyaluronic acid content'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Frozen/thawed and fresh uninjured mouse spinal cord preparations did not differ significantly in measured elastic modulus.',
    'Pa',
    'Frozen/thawed and fresh uninjured mouse spinal cord preparations did not differ significantly in measured elastic modulus.',
    'sample preparation comparison showed no significant difference',
    'Results / Figure 1',
    'Fig 1',
    'high',
    '{"curator_notes": "Important method-control observation because Cooper used 10 um cryosections on slides.", "paper_tracker_id": "M1A-P027", "quantitative": "YES", "statistics_reported": "p = 0.3823; Mann-Whitney test", "topic_id": "M1B-T004", "tracker_id": "M1B-O006"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P027-E001'
    AND et.evidence_type_name = 'AFM microindentation'
    AND ot.outcome_type_name = 'Method validation'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chronic severe mouse contusion lesion regions were stiffer than uninjured spinal cord.',
    'Pa',
    'Chronic severe mouse contusion lesion regions were stiffer than uninjured spinal cord.',
    'chronic contusion stiffening vs uninjured',
    'Results / Figure 2',
    'Fig 2',
    'high',
    '{"curator_notes": "Severe T11 contusion, 12 WPI, female C57BL/6 mice.", "paper_tracker_id": "M1A-P027", "quantitative": "YES", "statistics_reported": "significance reported in Fig 2 / source tables", "topic_id": "M1B-T004", "tracker_id": "M1B-O007"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P027-E002'
    AND et.evidence_type_name = 'AFM microindentation'
    AND ot.outcome_type_name = 'Young''s modulus'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Mouse and human astrocytes cultured on 2000 Pa substrate showed stiffness-associated morphology changes relative to 200 Pa substrate.',
    'Pa substrate stiffness',
    'Mouse and human astrocytes cultured on 2000 Pa substrate showed stiffness-associated morphology changes relative to 200 Pa substrate.',
    'astrocytes respond to scar-range stiffness',
    'Results / Figures 3-4',
    'Fig 3-Fig 4',
    'high',
    '{"curator_notes": "Supports plausibility that tissue mechanics can influence glial phenotype; source quote: \"2000 Pa substrate\".", "paper_tracker_id": "M1A-P027", "quantitative": "YES", "statistics_reported": "human circularity p < 0.01; complexity p < 0.0001", "topic_id": "M1B-T004", "tracker_id": "M1B-O008"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P027-E003'
    AND et.evidence_type_name = 'Cell culture morphology'
    AND ot.outcome_type_name = 'Astrocyte mechanosensitivity'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Overall lesion-site stiffness after IMP treatment was 517 Pa versus 1217 Pa in saline-treated injured mice and 405 Pa in uninjured spinal cord.',
    'Pa',
    'Overall lesion-site stiffness after IMP treatment was 517 Pa versus 1217 Pa in saline-treated injured mice and 405 Pa in uninjured spinal cord.',
    'IMP reduced chronic lesion stiffness toward uninjured values',
    'Results / Figure 5',
    'Fig 5B',
    'high',
    '{"curator_notes": "Directly links reduced fibrotic scarring intervention to reduced stiffness.", "paper_tracker_id": "M1A-P027", "quantitative": "YES", "statistics_reported": "p = 0.0180; Kruskal-Wallis test", "topic_id": "M1B-T004", "tracker_id": "M1B-O009"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P027-E004'
    AND et.evidence_type_name = 'AFM microindentation'
    AND ot.outcome_type_name = 'Young''s modulus after treatment'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In IMP-treated mice, lesion rim was stiffer than lesion core: 601 Pa versus 434 Pa.',
    'Pa',
    'In IMP-treated mice, lesion rim was stiffer than lesion core: 601 Pa versus 434 Pa.',
    'IMP-treated rim > core stiffness',
    'Results / Figure 5',
    'Fig 5C-D',
    'high',
    '{"curator_notes": "Indicates subregion mechanics remain spatially heterogeneous after treatment.", "paper_tracker_id": "M1A-P027", "quantitative": "YES", "statistics_reported": "p = 0.0432; Mann-Whitney test", "topic_id": "M1B-T004", "tracker_id": "M1B-O010"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P027-E004'
    AND et.evidence_type_name = 'AFM microindentation'
    AND ot.outcome_type_name = 'Lesion subregion stiffness'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Saline-treated chronic contusion scars showed highly aligned GFAP-positive fibers; IMP-treated tissue had reduced alignment approaching uninjured controls.',
    'alignment coefficient',
    'Saline-treated chronic contusion scars showed highly aligned GFAP-positive fibers; IMP-treated tissue had reduced alignment approaching uninjured controls.',
    'IMP reduced pathological glial fiber alignment',
    'Results / Figure 6',
    'Fig 6',
    'high',
    '{"curator_notes": "CurveAlign measured glial/fibrotic interface alignment; source quote: \"p < 0.01\".", "paper_tracker_id": "M1A-P027", "quantitative": "YES", "statistics_reported": "p < 0.01; one-way ANOVA with Tukey post hoc; n = 5 mice/group", "topic_id": "M1B-T004", "tracker_id": "M1B-O011"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P027-E004'
    AND et.evidence_type_name = 'Image analysis / GFAP alignment'
    AND ot.outcome_type_name = 'Glial fiber alignment'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In uninjured mouse spinal cord, Col1alpha1-positive cells localized mainly along larger blood vessels, expressed CD13 and PDGFRbeta, and lacked NG2, nestin, alphaSMA, immune, endothelial, astrocyte, oligodendrocyte, and fibrocyte markers.',
    'percent marker overlap / qualitative location',
    'In uninjured mouse spinal cord, Col1alpha1-positive cells localized mainly along larger blood vessels, expressed CD13 and PDGFRbeta, and lacked NG2, nestin, alphaSMA, immune, endothelial, astrocyte, oligodendrocyte, and fibrocyte markers.',
    'Col1alpha1-positive perivascular fibroblast-like baseline population',
    'Results / Figure 1',
    'Fig 1A-M',
    'high',
    '{"curator_notes": "Supports distinction from NG2/nestin pericyte marker profile; source quote: \"preferentially around larger-diameter blood vessels\".", "paper_tracker_id": "M1A-P008", "quantitative": "YES", "statistics_reported": "60.9 +/- 5.1% around smooth muscle cells; 78.7% CD13-positive; 95.7% PDGFRbeta-positive", "topic_id": "M1B-T002", "tracker_id": "M1B-O012"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P008-E001'
    AND et.evidence_type_name = 'LSFM / immunophenotyping'
    AND ot.outcome_type_name = 'Baseline scar-lineage identity'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'After T8 contusion, Col1alpha1-positive cells accumulated from 4-5 DPI, peaked at 7 DPI, and by 14 DPI formed a fibrous scar apposed to the GFAP-positive astrocytic border; 5-HT axons did not penetrate the Col1alpha1-positive region.',
    'days post injury / qualitative boundary',
    'After T8 contusion, Col1alpha1-positive cells accumulated from 4-5 DPI, peaked at 7 DPI, and by 14 DPI formed a fibrous scar apposed to the GFAP-positive astrocytic border; 5-HT axons did not penetrate the Col1alpha1-positive region.',
    'delayed Col1alpha1-positive fibrotic scar formation with axon-excluding border',
    'Results / Figure 2',
    'Fig 2A-H, K-M',
    'high',
    '{"curator_notes": "Female Col1alpha1-GFP mice, 75 kdyn T8 contusion, dura largely intact.", "paper_tracker_id": "M1A-P008", "quantitative": "YES", "statistics_reported": "one-way ANOVA, p < 0.0001 for cell-density time course", "topic_id": "M1B-T002", "tracker_id": "M1B-O013"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P008-E002'
    AND et.evidence_type_name = 'Time-course IHC / LSFM'
    AND ot.outcome_type_name = 'Fibrotic scar organization'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Col1alpha1-positive scar cells remained broadly PDGFRbeta-positive after contusion, CD13 expression decreased by 14 DPI, alphaSMA was transient and low by 14 DPI, and nonfibroblast lineage markers remained absent.',
    'percent marker overlap',
    'Col1alpha1-positive scar cells remained broadly PDGFRbeta-positive after contusion, CD13 expression decreased by 14 DPI, alphaSMA was transient and low by 14 DPI, and nonfibroblast lineage markers remained absent.',
    'PDGFRbeta-positive Col1alpha1 scar cells with dynamic CD13/alphaSMA phenotype',
    'Results / Figure 3',
    'Fig 3A-O',
    'high',
    '{"curator_notes": "Important because PDGFRbeta labels multiple perivascular populations and cannot alone define origin.", "paper_tracker_id": "M1A-P008", "quantitative": "YES", "statistics_reported": "100% PDGFRbeta-positive; 26.9% CD13-positive at 14 DPI; about 3.09% alphaSMA-positive at 14 DPI", "topic_id": "M1B-T002", "tracker_id": "M1B-O014"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P008-E003'
    AND et.evidence_type_name = 'Immunophenotyping'
    AND ot.outcome_type_name = 'Injury-induced marker shift'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Dorsal hemisection and contusion had similar timing of Col1alpha1-positive cell accumulation, but hemisection produced a Col1alpha1-positive scar continuous with dura and a laminin distribution throughout the injury site rather than mainly peripheral rim.',
    'qualitative model comparison',
    'Dorsal hemisection and contusion had similar timing of Col1alpha1-positive cell accumulation, but hemisection produced a Col1alpha1-positive scar continuous with dura and a laminin distribution throughout the injury site rather than mainly peripheral rim.',
    'dural disruption shifts fibrotic scar geometry toward meningeal continuity',
    'Results / Figure 2',
    'Fig 2I-J, O-V',
    'high',
    '{"curator_notes": "Boundary condition for contusion versus penetrating injury origin.", "paper_tracker_id": "M1A-P008", "quantitative": "YES", "statistics_reported": "n = 3 per dorsal hemisection time point", "topic_id": "M1B-T002", "tracker_id": "M1B-O015"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P008-E004'
    AND et.evidence_type_name = 'Comparative histology'
    AND ot.outcome_type_name = 'Injury-model scar geometry'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NG2-lineage cells localized mostly outside the Col1alpha1-positive injury epicenter after contusion, and red NG2-lineage cells rarely overlapped with green Col1alpha1-positive scar cells.',
    'qualitative lineage overlap',
    'NG2-lineage cells localized mostly outside the Col1alpha1-positive injury epicenter after contusion, and red NG2-lineage cells rarely overlapped with green Col1alpha1-positive scar cells.',
    'NG2-positive pericytes/OPCs not major Col1alpha1-positive scar source',
    'Results / Figure 4',
    'Fig 4A-L',
    'high',
    '{"curator_notes": "Authors caution NG2-CreER labels only a fraction of NG2-positive pericytes.", "paper_tracker_id": "M1A-P008", "quantitative": "YES", "statistics_reported": "n = 3 at 14 DPI; rare overlap noted", "topic_id": "M1B-T002", "tracker_id": "M1B-O016"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P008-E005'
    AND et.evidence_type_name = 'NG2-CreER lineage tracing'
    AND ot.outcome_type_name = 'Pericyte contribution'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tamoxifen-induced Glast-Rasless recombination reduced PDGFRbeta-positive stromal scar occupancy after dorsal hemisection; complete blockade in 3 of 12 tamoxifen-treated mice caused failure to close the injury site, whereas 9 of 12 showed partial attenuation with tissue integrity.',
    'proportion / qualitative phenotype',
    'Tamoxifen-induced Glast-Rasless recombination reduced PDGFRbeta-positive stromal scar occupancy after dorsal hemisection; complete blockade in 3 of 12 tamoxifen-treated mice caused failure to close the injury site, whereas 9 of 12 showed partial attenuation with tissue integrity.',
    'partial type A pericyte-derived scar reduction; complete block produces tissue defect',
    'Results / Figure 1',
    'Fig 1A-G',
    'high',
    '{"curator_notes": "Separates beneficial attenuation from harmful ablation.", "paper_tracker_id": "M1A-P009", "quantitative": "YES", "statistics_reported": "3/12 Tam-def; 9/12 Tam intermediate; PDGFRbeta scar occupancy quantified", "topic_id": "M1B-T002", "tracker_id": "M1B-O017"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P009-E001'
    AND et.evidence_type_name = 'Genetic attenuation / histology'
    AND ot.outcome_type_name = 'Fibrotic scar occupancy'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'At 2 WPI, vehicle versus tamoxifen lesion RNA-seq identified 1,099 differentially expressed genes enriched for ECM organization, collagen fibril organization, adhesion, angiogenesis, and wound healing; fibrosis-associated genes were reduced in Tam animals and clustered with uninjured profiles.',
    'differential expression',
    'At 2 WPI, vehicle versus tamoxifen lesion RNA-seq identified 1,099 differentially expressed genes enriched for ECM organization, collagen fibril organization, adhesion, angiogenesis, and wound healing; fibrosis-associated genes were reduced in Tam animals and clustered with uninjured profiles.',
    'broad ECM/fibrosis transcriptional program depends on type A pericyte progeny',
    'Results / Figure 1',
    'Fig 1E-G, Fig S2',
    'high',
    '{"curator_notes": "Supports mechanism beyond PDGFRbeta area alone.", "paper_tracker_id": "M1A-P009", "quantitative": "YES", "statistics_reported": "FDR-adjusted p < 0.05; fold change > +/-1.5", "topic_id": "M1B-T002", "tracker_id": "M1B-O018"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P009-E001'
    AND et.evidence_type_name = 'RNA-seq / ECM validation'
    AND ot.outcome_type_name = 'Fibrosis program'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Moderate reduction of pericyte-derived scarring reduced CST dieback/retraction features and allowed CST axons to enter or extend beyond lesion tissue at chronic time points, whereas vehicle and tissue-defect animals showed little or no regeneration.',
    'percent traced CST axons / distance',
    'Moderate reduction of pericyte-derived scarring reduced CST dieback/retraction features and allowed CST axons to enter or extend beyond lesion tissue at chronic time points, whereas vehicle and tissue-defect animals showed little or no regeneration.',
    'moderate scar attenuation permits CST regeneration',
    'Results / Figures 2-4',
    'Fig 2-Fig 4',
    'high',
    '{"curator_notes": "Tam-def tissue defects did not improve CST regeneration, reinforcing the partial-attenuation boundary.", "paper_tracker_id": "M1A-P009", "quantitative": "YES", "statistics_reported": "10.5 +/- 2.1% traced CST axons reached lesion site in Tam animals at 18 WPI", "topic_id": "M1B-T002", "tracker_id": "M1B-O019"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P009-E002'
    AND et.evidence_type_name = 'Axon tracing / IHC'
    AND ot.outcome_type_name = 'Axonal regeneration'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In scar-attenuated mice with ChR2-labeled CST axons, photostimulation evoked postsynaptic activity caudal to the lesion, supporting functional integration of regenerated CST projections.',
    'electrophysiological response',
    'In scar-attenuated mice with ChR2-labeled CST axons, photostimulation evoked postsynaptic activity caudal to the lesion, supporting functional integration of regenerated CST projections.',
    'regenerated CST axons functionally integrate below lesion',
    'Results / Figures 5-6',
    'Fig 5-Fig 6',
    'high',
    '{"curator_notes": "Source conclusion links regenerated axons to local spinal circuitry below lesion.", "paper_tracker_id": "M1A-P009", "quantitative": "YES", "statistics_reported": "electrophysiology and optogenetic stimulation reported", "topic_id": "M1B-T002", "tracker_id": "M1B-O020"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P009-E003'
    AND et.evidence_type_name = 'Optogenetics / electrophysiology'
    AND ot.outcome_type_name = 'Circuit integration'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Animals with attenuated pericyte-derived scarring showed improved sensorimotor recovery, and regenerated axon number correlated with behavioral improvement.',
    'behavioral score / correlation',
    'Animals with attenuated pericyte-derived scarring showed improved sensorimotor recovery, and regenerated axon number correlated with behavioral improvement.',
    'scar attenuation-associated axon growth tracks recovery',
    'Results / Figure 7',
    'Fig 7A-H',
    'high',
    '{"curator_notes": "Behavioral analysis excluded animals with spared CST fibers and tissue defects.", "paper_tracker_id": "M1A-P009", "quantitative": "YES", "statistics_reported": "correlation analyses reported; horizontal ladder, CatWalk, and ChR2-assisted behavior used", "topic_id": "M1B-T002", "tracker_id": "M1B-O021"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P009-E004'
    AND et.evidence_type_name = 'Behavioral assays / correlation'
    AND ot.outcome_type_name = 'Functional recovery'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'PDGFRbeta-lineage cells were recruited into lesion cores after both transection and crush SCI, with higher density after transection; many proliferated at 5 DPI and about half were BrdU-positive by 14 DPI.',
    'cell density / percent proliferation',
    'PDGFRbeta-lineage cells were recruited into lesion cores after both transection and crush SCI, with higher density after transection; many proliferated at 5 DPI and about half were BrdU-positive by 14 DPI.',
    'PDGFRbeta-positive stromal recruitment is injury-model dependent',
    'Results / Figure 1',
    'Fig 1A-I',
    'high',
    '{"curator_notes": "Transection is penetrating; crush is non-penetrating with intact dura.", "paper_tracker_id": "M1A-P021", "quantitative": "YES", "statistics_reported": "49.18 +/- 2.86% Ki67-positive after transection and 43.26 +/- 2.24% after crush at 5 DPI", "topic_id": "M1B-T002", "tracker_id": "M1B-O022"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P021-E001'
    AND et.evidence_type_name = 'PDGFRbeta lineage tracing / IHC'
    AND ot.outcome_type_name = 'Injury-model recruitment'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'PDGFRbeta-positive lesion cells included fibroblasts, dividing fibroblasts, and pericytes/vSMCs, but Col1a2-lineage fibroblasts overlapped strongly with Col1-positive scar regions whereas Myh11- and NG2-lineage pericyte/vSMC cells contributed little to the lesion core.',
    'cell cluster / lineage overlap',
    'PDGFRbeta-positive lesion cells included fibroblasts, dividing fibroblasts, and pericytes/vSMCs, but Col1a2-lineage fibroblasts overlapped strongly with Col1-positive scar regions whereas Myh11- and NG2-lineage pericyte/vSMC cells contributed little to the lesion core.',
    'fibroblasts, not Myh11/NG2 pericytes/vSMCs, primary scar source in this lineage system',
    'Results / Figures 2-3',
    'Fig 2-Fig 3',
    'high',
    '{"curator_notes": "Directly boundary-checks pericyte/vSMC interpretation.", "paper_tracker_id": "M1A-P021", "quantitative": "YES", "statistics_reported": "44,386 PDGFRbeta-lineage scRNA-seq cells; lineage-density comparisons reported", "topic_id": "M1B-T002", "tracker_id": "M1B-O023"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P021-E002'
    AND et.evidence_type_name = 'scRNA-seq / lineage tracing'
    AND ot.outcome_type_name = 'Scar-cell source'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Meningeal Crabp2/Emb fibroblasts localized mainly to central fibrotic scar regions, while perivascular/pial Lama1/Lama2 fibroblasts localized mainly to peripheral/perivascular scar regions after transection and crush SCI.',
    'spatial compartment',
    'Meningeal Crabp2/Emb fibroblasts localized mainly to central fibrotic scar regions, while perivascular/pial Lama1/Lama2 fibroblasts localized mainly to peripheral/perivascular scar regions after transection and crush SCI.',
    'CE-F central; LA-F peripheral/perivascular',
    'Results / Figure 4',
    'Fig 4A-E',
    'high',
    '{"curator_notes": "Adds subcompartment structure within the fibrotic scar.", "paper_tracker_id": "M1A-P021", "quantitative": "YES", "statistics_reported": "Emb/Lama1 and Crabp2/Lama2 areas quantified at 14 DPI", "topic_id": "M1B-T002", "tracker_id": "M1B-O024"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P021-E003'
    AND et.evidence_type_name = 'Spatial marker mapping'
    AND ot.outcome_type_name = 'Fibroblast subtype organization'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Rhesus macaque transection lesions showed fibroblast subtype organization comparable to mouse SCI, including CE-F-like and LA-F-like populations in lesion core/edge samples.',
    'cross-species cell-state comparison',
    'Rhesus macaque transection lesions showed fibroblast subtype organization comparable to mouse SCI, including CE-F-like and LA-F-like populations in lesion core/edge samples.',
    'mouse fibroblast scar subtypes have monkey analogs',
    'Results / Figure 6',
    'Fig 6A-H',
    'high',
    '{"curator_notes": "Supports translational relevance but in complete transection monkey model.", "paper_tracker_id": "M1A-P021", "quantitative": "YES", "statistics_reported": "female rhesus macaques sampled at 0, 7, 14, 30 DPI, and 6 MPI", "topic_id": "M1B-T002", "tracker_id": "M1B-O025"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P021-E004'
    AND et.evidence_type_name = 'Monkey scRNA/snRNA-seq / IHC'
    AND ot.outcome_type_name = 'Cross-species conservation'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O025', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'CE-F showed stronger cholesterol synthesis and type I collagen/fibronectin programs, while LA-F showed laminin/type IV collagen, lipid transport/storage, and angiogenesis-associated function including stronger endothelial tube formation support.',
    'gene program / functional assay',
    'CE-F showed stronger cholesterol synthesis and type I collagen/fibronectin programs, while LA-F showed laminin/type IV collagen, lipid transport/storage, and angiogenesis-associated function including stronger endothelial tube formation support.',
    'CE-F and LA-F have distinct ECM/metabolic/vascular functions',
    'Results / Figures 7-8',
    'Fig 7-Fig 8',
    'high',
    '{"curator_notes": "Functionalizes scar compartments instead of treating fibrosis as one cell state.", "paper_tracker_id": "M1A-P021", "quantitative": "YES", "statistics_reported": "GO enrichment, Bodipy/myelin uptake, RT-qPCR, tube formation, and ligand-receptor analyses reported", "topic_id": "M1B-T002", "tracker_id": "M1B-O026"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P021-E005'
    AND et.evidence_type_name = 'Pathway analysis / in vitro assays'
    AND ot.outcome_type_name = 'Fibroblast subtype function'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O026', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'After T9 contusion, GFAP-positive astrocytic scar area and astrocyte process overlap increased over time and persisted to 12 WPI; chronic astrocytes differed transcriptionally from subacute scar-forming astrocytes.',
    'area / process overlap / qPCR',
    'After T9 contusion, GFAP-positive astrocytic scar area and astrocyte process overlap increased over time and persisted to 12 WPI; chronic astrocytes differed transcriptionally from subacute scar-forming astrocytes.',
    'chronic glial scar persists but changes phenotype over time',
    'Results / Figure 1',
    'Fig 1A-E',
    'high',
    '{"curator_notes": "Chronic astrocytes had higher Sox9 but lower Cdh2, Csgalanact1, and Pcan than 2 WPI scar-forming astrocytes.", "paper_tracker_id": "M1A-P003", "quantitative": "YES", "statistics_reported": "p < 0.05 threshold; group comparisons reported", "topic_id": "M1B-T003", "tracker_id": "M1B-O027"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P003-E001'
    AND et.evidence_type_name = 'Histology / LMD-qPCR'
    AND ot.outcome_type_name = 'Chronic astrocytic scar persistence'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O027', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'IL-6 reactive astrocytes converted to collagen-I-grown scar-forming astrocytes on type I collagen; after reseeding onto Poly-D-lysine, Col-I-SAs retained flattened morphology, N-cadherin expression, and SA-marker gene expression.',
    'qPCR / morphology',
    'IL-6 reactive astrocytes converted to collagen-I-grown scar-forming astrocytes on type I collagen; after reseeding onto Poly-D-lysine, Col-I-SAs retained flattened morphology, N-cadherin expression, and SA-marker gene expression.',
    'once induced, Col-I-SA phenotype resists collagen-signal withdrawal',
    'Results / Figure 2',
    'Fig 2A-F',
    'high',
    '{"curator_notes": "Indicates scar-forming astrocyte state is not simply reversed by removing the initiating collagen surface.", "paper_tracker_id": "M1A-P003", "quantitative": "YES", "statistics_reported": "n = 6 wells per group; ANOVA/Tukey-Kramer and Wilcoxon tests", "topic_id": "M1B-T003", "tracker_id": "M1B-O028"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P003-E002'
    AND et.evidence_type_name = 'In vitro astrocyte culture'
    AND ot.outcome_type_name = 'Scar-forming astrocyte stability'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O028', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Anti-beta1-integrin or N-cadherin-neutralizing antibody treatment did not revert Col-I-SA morphology or SA-marker gene expression to reactive or naive astrocyte states in vitro.',
    'qPCR / morphology',
    'Anti-beta1-integrin or N-cadherin-neutralizing antibody treatment did not revert Col-I-SA morphology or SA-marker gene expression to reactive or naive astrocyte states in vitro.',
    'established Col-I-SAs resist beta1-integrin/N-cadherin blockade in vitro',
    'Results / Figure 3',
    'Fig 3A-D',
    'high',
    '{"curator_notes": "Distinguishes prevention of transformation from reversal of established scar astrocytes.", "paper_tracker_id": "M1A-P003", "quantitative": "YES", "statistics_reported": "n = 6 wells per group; Wilcoxon rank-sum tests", "topic_id": "M1B-T003", "tracker_id": "M1B-O029"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P003-E003'
    AND et.evidence_type_name = 'In vitro antibody blockade'
    AND ot.outcome_type_name = 'Pathway robustness'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O029', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'EGFP-positive Col-I-SAs transplanted into naive spinal cord formed N-cadherin-rich astroglial scar-like clusters and induced nearby host GFAP-positive astrocytes to express SA-associated genes.',
    'qPCR / IHC',
    'EGFP-positive Col-I-SAs transplanted into naive spinal cord formed N-cadherin-rich astroglial scar-like clusters and induced nearby host GFAP-positive astrocytes to express SA-associated genes.',
    'scar-forming astrocytes self-maintain and recruit adjacent astrocytes',
    'Results / Figure 4',
    'Fig 4A-F',
    'high',
    '{"curator_notes": "Host astrocytes increased Cdh2, Sox9, Acan, and Pcan after transplantation.", "paper_tracker_id": "M1A-P003", "quantitative": "YES", "statistics_reported": "n = 6 mice per group; Wilcoxon rank-sum tests", "topic_id": "M1B-T003", "tracker_id": "M1B-O030"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P003-E004'
    AND et.evidence_type_name = 'Astrocyte transplantation / LMD-qPCR'
    AND ot.outcome_type_name = 'Scar-forming astrocyte recruitment'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O030', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Anti-beta1-integrin antibody blocked recruitment of host scar-forming astrocytes after SA transplantation and, when injected from 14-28 DPI after SCI, reduced GFAP/N-cadherin-positive chronic astrocytes and increased GAP43-positive area.',
    'cell count / area',
    'Anti-beta1-integrin antibody blocked recruitment of host scar-forming astrocytes after SA transplantation and, when injected from 14-28 DPI after SCI, reduced GFAP/N-cadherin-positive chronic astrocytes and increased GAP43-positive area.',
    'beta1-integrin blockade reduces chronic SA recruitment and increases GAP43 signal',
    'Results / Figure 5',
    'Fig 5A-H',
    'high',
    '{"curator_notes": "Supports intervention on recruitment rather than direct in vitro reversion.", "paper_tracker_id": "M1A-P003", "quantitative": "YES", "statistics_reported": "n = 6 mice per group; Wilcoxon rank-sum tests; p < 0.05", "topic_id": "M1B-T003", "tracker_id": "M1B-O031"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P003-E005–E006'
    AND et.evidence_type_name = 'In vivo antibody treatment'
    AND ot.outcome_type_name = 'Chronic scar modulation / axon growth'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O031', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cx3cr1-CreER INTACT profiling identified temporal injury-activated microglia/macrophage signatures at 3, 7, and 14 DPI after T8 dorsal column transection.',
    'RNA-seq time course',
    'Cx3cr1-CreER INTACT profiling identified temporal injury-activated microglia/macrophage signatures at 3, 7, and 14 DPI after T8 dorsal column transection.',
    'temporal IAM program after SCI',
    'Source page / Module 1A row',
    'Fig 1 / source page',
    'medium',
    '{"curator_notes": "Included because astrocytic border formation is coupled to immune corralling and wound compaction.", "paper_tracker_id": "M1A-P030", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T003", "tracker_id": "M1B-O032"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P030-E001'
    AND et.evidence_type_name = 'Myeloid nuclear RNA-seq'
    AND ot.outcome_type_name = 'Injury-activated myeloid state'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O032', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Myeloid Plexin-B2 deletion disrupted lesion-core corralling, astrocytic border containment, matrix compaction, inflammatory restriction, axon regeneration, and motor-sensory recovery after dorsal column transection.',
    'qualitative + functional assays',
    'Myeloid Plexin-B2 deletion disrupted lesion-core corralling, astrocytic border containment, matrix compaction, inflammatory restriction, axon regeneration, and motor-sensory recovery after dorsal column transection.',
    'myeloid Plexin-B2 promotes wound compaction and astrocytic containment',
    'Source page / Module 1A row',
    'Fig 2-Fig 7 / source page',
    'medium',
    '{"curator_notes": "Bridges M1B-T003 with immune-glial containment topic M1B-T008.", "paper_tracker_id": "M1A-P030", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T003", "tracker_id": "M1B-O033"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P030-E002'
    AND et.evidence_type_name = 'Conditional deletion / histology / function'
    AND ot.outcome_type_name = 'Corralling and containment'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O033', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Source-page extraction reports that astrocytic Ryk is induced after SCI and that astrocyte-focused Ryk perturbation alters morphological transformation, scarring, wound architecture, and lesion-core containment.',
    'source-page qualitative',
    'Source-page extraction reports that astrocytic Ryk is induced after SCI and that astrocyte-focused Ryk perturbation alters morphological transformation, scarring, wound architecture, and lesion-core containment.',
    'astrocytic Ryk coordinates border formation and wound healing',
    'Abstract / source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Needs full-text parsing before high-confidence observation materialization.", "paper_tracker_id": "M1A-P032", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T003", "tracker_id": "M1B-O034"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P032-E001–E002'
    AND et.evidence_type_name = 'Astrocyte signaling perturbation'
    AND ot.outcome_type_name = 'Border morphology / wound architecture'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O034', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Source-page extraction reports that border-forming astrocytes after SCI or stroke arise mainly from local astrocytes, with a minority contribution from OPC-derived astrocytes.',
    'source-page lineage proportion',
    'Source-page extraction reports that border-forming astrocytes after SCI or stroke arise mainly from local astrocytes, with a minority contribution from OPC-derived astrocytes.',
    'local astrocytes are major border-forming source; OPCs minor source',
    'Abstract / source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Complements Tamaru''s recruitment model with origin tracing.", "paper_tracker_id": "M1A-P033", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T003", "tracker_id": "M1B-O035"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P033-E001'
    AND et.evidence_type_name = 'Lineage analysis'
    AND ot.outcome_type_name = 'Border astrocyte origin'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O035', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Source-page extraction reports temporal transcriptomic and single-nucleus RNA-seq definition of border-forming wound repair astrocyte programs after SCI/stroke.',
    'source-page transcriptomic program',
    'Source-page extraction reports temporal transcriptomic and single-nucleus RNA-seq definition of border-forming wound repair astrocyte programs after SCI/stroke.',
    'border astrocytes are a wound-repair transcriptional state',
    'Abstract / source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Supports classification of astrocytic scar as an active wound-repair compartment.", "paper_tracker_id": "M1A-P033", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T003", "tracker_id": "M1B-O036"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P033-E002'
    AND et.evidence_type_name = 'snRNA-seq / temporal transcriptomics'
    AND ot.outcome_type_name = 'Wound-repair astrocyte state'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O036', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gong generated a T10 lateral hemisection spatial transcriptomic atlas across 3, 7, 14, and 28 DPI using 32 sections and 15,449 spots, mapping clusters back to tissue morphology to define scar regions.',
    'spatial spots / time course',
    'Gong generated a T10 lateral hemisection spatial transcriptomic atlas across 3, 7, 14, and 28 DPI using 32 sections and 15,449 spots, mapping clusters back to tissue morphology to define scar regions.',
    'spatially mapped scar maturation atlas',
    'Results / Figure 1',
    'Fig 1A-L',
    'high',
    '{"curator_notes": "Provides architecture scaffold for Module 1B compartment definitions.", "paper_tracker_id": "M1A-P004", "quantitative": "YES", "statistics_reported": "32 sections; 15,449 spots; 3, 7, 14, 28 DPI", "topic_id": "M1B-T001", "tracker_id": "M1B-O037"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P004-E001'
    AND et.evidence_type_name = 'Spatial transcriptomics / H&E'
    AND ot.outcome_type_name = 'Scar spatial atlas'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O037', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Reclustered scar spots resolved six major scar-resident cell groups: microglia, macrophages, astrocytes, oligodendrocytes, fibroblasts, and endothelial cells; fibroblasts occupied the scar center from 7 DPI, with microglia, astrocytes, and oligodendrocytes arranged outward toward the boundary.',
    'cell-state spatial distribution',
    'Reclustered scar spots resolved six major scar-resident cell groups: microglia, macrophages, astrocytes, oligodendrocytes, fibroblasts, and endothelial cells; fibroblasts occupied the scar center from 7 DPI, with microglia, astrocytes, and oligodendrocytes arranged outward toward the boundary.',
    'multicellular scar with fibroblast core and glial/immune boundary layers',
    'Results / Figures 2-8',
    'Fig 2-Fig 8',
    'high',
    '{"curator_notes": "Source also notes very few neurons in the scar area.", "paper_tracker_id": "M1A-P004", "quantitative": "YES", "statistics_reported": "Scar-cell fractions quantified across maturation stages", "topic_id": "M1B-T001", "tracker_id": "M1B-O038"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P004-E002'
    AND et.evidence_type_name = 'ST reclustering / marker mapping'
    AND ot.outcome_type_name = 'Scar-resident cell composition'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O038', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Laminin, Fn1, collagen IV staining and ST maps showed changing scar marker distributions; fibroblasts remained central during shrinkage/maturation, while microglial and astrocytic scar regions expanded along white matter at 28 DPI.',
    'spatial marker map / cell fraction',
    'Laminin, Fn1, collagen IV staining and ST maps showed changing scar marker distributions; fibroblasts remained central during shrinkage/maturation, while microglial and astrocytic scar regions expanded along white matter at 28 DPI.',
    'ECM marker maps define dynamic scar boundary and subcompartments',
    'Results / Figure 10',
    'Fig 10A-F',
    'high',
    '{"curator_notes": "Confirms fibrotic scar surrounded by microglial scar wrapped by astrocytic scar in this model.", "paper_tracker_id": "M1A-P004", "quantitative": "YES", "statistics_reported": "Cell-type spot counts and fractions quantified", "topic_id": "M1B-T001", "tracker_id": "M1B-O039"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P004-E004'
    AND et.evidence_type_name = 'Tissue transparency / ST marker maps'
    AND ot.outcome_type_name = 'Scar boundary markers'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O039', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gong proposed four scar-formation phases after lateral hemisection: macrophage infiltration, proliferation/differentiation of scar-resident cells, scar emergence, and stationary scar.',
    'phase classification',
    'Gong proposed four scar-formation phases after lateral hemisection: macrophage infiltration, proliferation/differentiation of scar-resident cells, scar emergence, and stationary scar.',
    'four-phase scar maturation model',
    'Results / Discussion',
    'Fig 9-Fig 10G',
    'medium',
    '{"curator_notes": "Interpretive synthesis from spatial transcriptomics, not a direct single assay.", "paper_tracker_id": "M1A-P004", "quantitative": "NO", "statistics_reported": "WGCNA modules and cell-fraction trajectories support synthesis", "topic_id": "M1B-T001", "tracker_id": "M1B-O040"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P004-E003–E004'
    AND et.evidence_type_name = 'WGCNA / phase synthesis'
    AND ot.outcome_type_name = 'Scar maturation phase model'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O040', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'FnEDA and FnEDB were low/detectable in uninjured spinal cord, rose sharply after T11 contusion, and remained elevated even 13 weeks after injury.',
    'fold-change / protein level',
    'FnEDA and FnEDB were low/detectable in uninjured spinal cord, rose sharply after T11 contusion, and remained elevated even 13 weeks after injury.',
    'persistent cellular fibronectin isoform expression after SCI',
    'Results / Figure 1',
    'Fig 1A-G',
    'high',
    '{"curator_notes": "FnEDA protein increased around 10-fold by 7 DPI and declined but remained elevated.", "paper_tracker_id": "M1A-P007", "quantitative": "YES", "statistics_reported": "FnEDA mRNA about 70-fold and FnEDB about 40-fold at 7 DPI; n = 8-10 for qPCR", "topic_id": "M1B-T001", "tracker_id": "M1B-O041"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P007-E001'
    AND et.evidence_type_name = 'qPCR / western blot'
    AND ot.outcome_type_name = 'Fibrotic ECM isoform time course'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O041', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'FnEDA-null mice had smaller GFAP-bounded lesion cores and lower fibronectin intensity inside the GFAP-negative lesion core at 90 DPI, while GFAP glial scarring was not reduced.',
    'lesion area / intensity',
    'FnEDA-null mice had smaller GFAP-bounded lesion cores and lower fibronectin intensity inside the GFAP-negative lesion core at 90 DPI, while GFAP glial scarring was not reduced.',
    'FnEDA deletion reduces chronic fibrotic core without reducing glial rim',
    'Results / Figure 2',
    'Fig 2A-I',
    'high',
    '{"curator_notes": "Supports separability of fibrotic core and astrocytic border compartments.", "paper_tracker_id": "M1A-P007", "quantitative": "YES", "statistics_reported": "lesion area p < 0.01; fibronectin intensity p < 0.01", "topic_id": "M1B-T001", "tracker_id": "M1B-O042"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P007-E002'
    AND et.evidence_type_name = 'IHC / western blot'
    AND ot.outcome_type_name = 'Chronic fibrotic scar anatomy'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O042', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'At 21 and 90 DPI, FnEDA-null mice had reduced insoluble matrix-assembled fibronectin while soluble fibronectin did not differ from wildtype.',
    'soluble/insoluble protein fraction',
    'At 21 and 90 DPI, FnEDA-null mice had reduced insoluble matrix-assembled fibronectin while soluble fibronectin did not differ from wildtype.',
    'FnEDA stabilizes chronic assembled fibronectin matrix',
    'Results / Figure 3',
    'Fig 3A-F',
    'high',
    '{"curator_notes": "No difference in soluble/insoluble fibronectin at 7 DPI.", "paper_tracker_id": "M1A-P007", "quantitative": "YES", "statistics_reported": "n = 7-8 mice/group; p < 0.01", "topic_id": "M1B-T001", "tracker_id": "M1B-O043"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P007-E003'
    AND et.evidence_type_name = 'DOC/SDS fractionation'
    AND ot.outcome_type_name = 'Matrix stability'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O043', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'FnEDA-null mice had higher SMI-312 axonal density in lesion areas at 90 DPI and improved locomotor recovery by BMS and modified BBB compared with wildtype controls.',
    'staining intensity / behavior score',
    'FnEDA-null mice had higher SMI-312 axonal density in lesion areas at 90 DPI and improved locomotor recovery by BMS and modified BBB compared with wildtype controls.',
    'reduced chronic fibrotic matrix associates with axon density and recovery',
    'Results / Figures 4-5',
    'Fig 4-Fig 5',
    'high',
    '{"curator_notes": "Functional link supports chronic fibrotic compartment as recovery-relevant.", "paper_tracker_id": "M1A-P007", "quantitative": "YES", "statistics_reported": "SMI-312 p < 0.05 or p < 0.01 by distance; behavior p < 0.05 to p < 0.001", "topic_id": "M1B-T001", "tracker_id": "M1B-O044"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P007-E004–E005'
    AND et.evidence_type_name = 'Axon staining / behavior'
    AND ot.outcome_type_name = 'Axon density and recovery'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O044', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Abstract-level extraction reports chronic rat contusion repaired tissue organized into fibrotic, cellular, and axonal zones, and scar ablation plus lamina propria/acellular lamina propria transplantation expanded cellular/axonal zones, reduced cavity, and improved integration with spared tissue.',
    'abstract-level qualitative',
    'Abstract-level extraction reports chronic rat contusion repaired tissue organized into fibrotic, cellular, and axonal zones, and scar ablation plus lamina propria/acellular lamina propria transplantation expanded cellular/axonal zones, reduced cavity, and improved integration with spared tissue.',
    'chronic repaired tissue has zone architecture modifiable by ablation/transplantation',
    'PubMed abstract / Module 1A row',
    'Abstract',
    'low',
    '{"curator_notes": "Full text needed before high-confidence materialization.", "paper_tracker_id": "M1A-P001", "quantitative": "YES", "statistics_reported": "Abstract-level only", "topic_id": "M1B-T001", "tracker_id": "M1B-O045"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P001-E001–E002'
    AND et.evidence_type_name = 'Light microscopy histology'
    AND ot.outcome_type_name = 'Chronic repaired-tissue zones'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O045', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Source-page extraction reports that single-cell RNA-seq resolved heterogeneous injured-spinal-cord scar-like cell states and inferred cell-cell interactions shaping the wound-healing/scar environment.',
    'source-page transcriptomic atlas',
    'Source-page extraction reports that single-cell RNA-seq resolved heterogeneous injured-spinal-cord scar-like cell states and inferred cell-cell interactions shaping the wound-healing/scar environment.',
    'scar is multicellular interaction ecosystem',
    'Abstract / source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Supports T001/T008 but needs full-text extraction for exact cell-state names.", "paper_tracker_id": "M1A-P031", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T001", "tracker_id": "M1B-O046"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P031-E001–E002'
    AND et.evidence_type_name = 'scRNA-seq / interaction inference'
    AND ot.outcome_type_name = 'Single-cell lesion ecology'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O046', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'After incomplete SCI, lesion-remote astrocytes in spared rostral and caudal cord acquired molecularly distinct, neuroanatomically restricted reactivity states across 3, 7, 14, and 28 DPI.',
    'transcriptomic state / time course',
    'After incomplete SCI, lesion-remote astrocytes in spared rostral and caudal cord acquired molecularly distinct, neuroanatomically restricted reactivity states across 3, 7, 14, and 28 DPI.',
    'lesion-remote astrocytes are heterogeneous spatial states',
    'Results / Figure 1',
    'Fig 1; Extended Data Fig 1-3',
    'high',
    '{"curator_notes": "Distinct from border-forming astrocytes and nontraumatic astrocyte states.", "paper_tracker_id": "M1A-P014", "quantitative": "YES", "statistics_reported": "n values reported per figure; multiple transcriptomic modalities", "topic_id": "M1B-T006", "tracker_id": "M1B-O047"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P014-E001'
    AND et.evidence_type_name = 'RiboTag / RNA-seq / snRNA-seq / spatial transcriptomics'
    AND ot.outcome_type_name = 'Lesion-remote astrocyte states'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O047', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'WM3/4 lesion-remote astrocytes co-localized with Mg2/Mg5 white matter degeneration-associated microglia in ipsilesional Wallerian-degenerating white matter.',
    'spatial co-localization / cell state',
    'WM3/4 lesion-remote astrocytes co-localized with Mg2/Mg5 white matter degeneration-associated microglia in ipsilesional Wallerian-degenerating white matter.',
    'WM3/4 LRA-WDM microglia niche',
    'Results / Figure 2',
    'Fig 2; Extended Data Fig 4-6',
    'high',
    '{"curator_notes": "Mg2/5 microglia phagocytose myelin debris and assemble into nodules.", "paper_tracker_id": "M1A-P014", "quantitative": "YES", "statistics_reported": "Spatial and snRNA-seq integration; WDM nodules quantified", "topic_id": "M1B-T006", "tracker_id": "M1B-O048"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P014-E002'
    AND et.evidence_type_name = 'Spatial transcriptomics / NMF'
    AND ot.outcome_type_name = 'White matter repair niche'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O048', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ccn1-positive white matter LRAs were restricted to Wallerian-degenerating white matter, neighbored debris-clearing WDM nodules, persisted to at least 90 DPI, and were required to restrain excessive/spatially aberrant microglial activation.',
    'cell count / spatial distribution',
    'Ccn1-positive white matter LRAs were restricted to Wallerian-degenerating white matter, neighbored debris-clearing WDM nodules, persisted to at least 90 DPI, and were required to restrain excessive/spatially aberrant microglial activation.',
    'Ccn1+ LRAs regulate WDM localization and magnitude',
    'Results / Figures 2-3',
    'Fig 2-Fig 3',
    'high',
    '{"curator_notes": "CCN1 loss amplified microglial response rather than eliminating it.", "paper_tracker_id": "M1A-P014", "quantitative": "YES", "statistics_reported": "WDM nodules up to about fourfold increased in Ccn1-cKO regions", "topic_id": "M1B-T006", "tracker_id": "M1B-O049"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P014-E002–E003'
    AND et.evidence_type_name = 'RNAscope / histology / conditional deletion'
    AND ot.outcome_type_name = 'CCN1 spatial regulation'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O049', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Astrocyte-specific Ccn1 deletion caused microglia to accumulate more internalized myelin and axon debris, attenuated debris clearance, and impaired neurological recovery after incomplete SCI.',
    'debris volume / behavior',
    'Astrocyte-specific Ccn1 deletion caused microglia to accumulate more internalized myelin and axon debris, attenuated debris clearance, and impaired neurological recovery after incomplete SCI.',
    'astrocyte CCN1 supports microglial debris processing and recovery',
    'Results / Figure 3',
    'Fig 3; Extended Data Fig 7',
    'high',
    '{"curator_notes": "Demonstrates remote white matter repair affects outcome.", "paper_tracker_id": "M1A-P014", "quantitative": "YES", "statistics_reported": "About 40% greater myelin debris and about 23% greater axon debris reported in Ccn1-cKO microglia", "topic_id": "M1B-T006", "tracker_id": "M1B-O050"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P014-E003'
    AND et.evidence_type_name = '3D debris reconstruction / behavior'
    AND ot.outcome_type_name = 'Debris clearance and recovery'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O050', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Recombinant CCN1 altered primary microglial lipid metabolism, including cholesterol efflux/lipid storage responses, supporting a mechanism for repair-associated lipid buffering.',
    'lipid assay / RNA-seq',
    'Recombinant CCN1 altered primary microglial lipid metabolism, including cholesterol efflux/lipid storage responses, supporting a mechanism for repair-associated lipid buffering.',
    'CCN1 modulates microglial lipid metabolism',
    'Results / Figure 4',
    'Fig 4; Extended Data Fig 8',
    'high',
    '{"curator_notes": "Mechanistic bridge from astrocyte secreted factor to debris-clearing microglia.", "paper_tracker_id": "M1A-P014", "quantitative": "YES", "statistics_reported": "RNA-seq, cholesterol efflux, LipidTOX, and lipidomics assays", "topic_id": "M1B-T006", "tracker_id": "M1B-O051"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P014-E004'
    AND et.evidence_type_name = 'Primary microglia / lipid assays'
    AND ot.outcome_type_name = 'Microglial lipid handling'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O051', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Local myelin damage induced Ccn1-positive astrocytes, and comparable white-matter damage-associated astrocyte patterns were observed across demyelinating models and human disorder tissue, including SCI-relevant lesion-remote white matter.',
    'cross-model / human tissue comparison',
    'Local myelin damage induced Ccn1-positive astrocytes, and comparable white-matter damage-associated astrocyte patterns were observed across demyelinating models and human disorder tissue, including SCI-relevant lesion-remote white matter.',
    'Ccn1+ white matter astrocyte response is damage-linked and conserved',
    'Results / Figure 5',
    'Fig 5; Extended Data Fig 9',
    'high',
    '{"curator_notes": "Supports generality beyond the primary incomplete SCI model.", "paper_tracker_id": "M1A-P014", "quantitative": "YES", "statistics_reported": "Multiple mouse injury/demyelination models and human tissues", "topic_id": "M1B-T006", "tracker_id": "M1B-O052"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P014-E005'
    AND et.evidence_type_name = 'Myelin damage models / human tissue comparison'
    AND ot.outcome_type_name = 'Conserved white matter astrocyte state'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O052', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In five rat spines 2 months after compressive SCI, 9.4T inversion-recovery-supported proton-density MRI depicted spared and injured white matter, lesion volume, and cord atrophy; MRI severity and white-matter sparing aligned with locomotor recovery and histology.',
    'MRI / histology / BBB',
    'In five rat spines 2 months after compressive SCI, 9.4T inversion-recovery-supported proton-density MRI depicted spared and injured white matter, lesion volume, and cord atrophy; MRI severity and white-matter sparing aligned with locomotor recovery and histology.',
    'spared white matter is MRI-visible and recovery-linked',
    'Abstract / source page',
    'Abstract / Nature page',
    'medium',
    '{"curator_notes": "Post-mortem MRI; not in vivo longitudinal imaging.", "paper_tracker_id": "M1A-P024", "quantitative": "YES", "statistics_reported": "n = 5 excised rat spines", "topic_id": "M1B-T006", "tracker_id": "M1B-O053"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P024-E001–E002'
    AND et.evidence_type_name = 'Post-mortem MRI / histology / BBB'
    AND ot.outcome_type_name = 'Spared white matter imaging'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O053', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Source-page extraction reports that 7.0T MRI tracked pathological variation in white matter tracts after severe thoracic contusion, and spared white matter/pathological tract variation related to hindlimb motor recovery.',
    'MRI metrics / motor recovery',
    'Source-page extraction reports that 7.0T MRI tracked pathological variation in white matter tracts after severe thoracic contusion, and spared white matter/pathological tract variation related to hindlimb motor recovery.',
    'MRI-visible white matter tract pathology relates to recovery',
    'Abstract / source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Full text needed for exact MRI metric values.", "paper_tracker_id": "M1A-P036", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T006", "tracker_id": "M1B-O054"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P036-E001–E002'
    AND et.evidence_type_name = 'In vivo MRI / pathology-function linkage'
    AND ot.outcome_type_name = 'White matter tract pathology'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O054', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Abstract-level extraction reports chronic changes in residual dorsal, lateral, and ventral funicular white matter cellular composition 6 WPI after contusion, with acute TTX treatment related to chronic axon density, function, and cellular composition.',
    'abstract-level qualitative',
    'Abstract-level extraction reports chronic changes in residual dorsal, lateral, and ventral funicular white matter cellular composition 6 WPI after contusion, with acute TTX treatment related to chronic axon density, function, and cellular composition.',
    'residual white matter has chronic cellular remodeling',
    'PubMed abstract / Module 1A row',
    'Abstract',
    'low',
    '{"curator_notes": "Full text needed before high-confidence materialization.", "paper_tracker_id": "M1A-P013", "quantitative": "YES", "statistics_reported": "Abstract-level only", "topic_id": "M1B-T006", "tracker_id": "M1B-O055"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P013-E001–E002'
    AND et.evidence_type_name = 'Histology / cellular composition'
    AND ot.outcome_type_name = 'Chronic residual white matter cellularity'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O055', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In adult female rat moderate contusion SCI, delayed 2 mm glial scar resection at 1 WPI produced significantly worse BBB locomotor scores than nonresection contusion controls and did not produce BDA-positive axons at or caudal to the lesion epicenter.',
    'BBB score / BDA axon index',
    'In adult female rat moderate contusion SCI, delayed 2 mm glial scar resection at 1 WPI produced significantly worse BBB locomotor scores than nonresection contusion controls and did not produce BDA-positive axons at or caudal to the lesion epicenter.',
    'scar resection alone worsened contusion recovery and did not restore axon crossing',
    'Results / Figures 1-4',
    'Fig 1-Fig 4',
    'high',
    '{"curator_notes": "Critical boundary condition against treating resection alone as inherently reparative.", "paper_tracker_id": "M1A-P005", "quantitative": "YES", "statistics_reported": "BBB p < 0.05 versus nonresection contusion; axon comparisons p values reported", "topic_id": "M1B-T005", "tracker_id": "M1B-O056"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P005-E001'
    AND et.evidence_type_name = 'Behavioral assay / BDA tract tracing'
    AND ot.outcome_type_name = 'Resection outcome after contusion'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O056', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In adult female rat dorsal hemisection SCI, delayed 2 mm glial scar resection at 1 WPI did not significantly change BBB locomotor scores versus nonresection hemisection controls, and no group showed BDA-positive axons at or caudal to the lesion epicenter.',
    'BBB score / BDA axon index',
    'In adult female rat dorsal hemisection SCI, delayed 2 mm glial scar resection at 1 WPI did not significantly change BBB locomotor scores versus nonresection hemisection controls, and no group showed BDA-positive axons at or caudal to the lesion epicenter.',
    'scar resection alone neutral after hemisection and insufficient for lesion crossing',
    'Results / Figures 1-4',
    'Fig 1-Fig 4',
    'high',
    '{"curator_notes": "Shows injury-model dependence and lack of axon-bridging benefit from resection alone.", "paper_tracker_id": "M1A-P005", "quantitative": "YES", "statistics_reported": "BBB p = 0.61 for resection versus nonresection hemisection; BDA comparisons reported", "topic_id": "M1B-T005", "tracker_id": "M1B-O057"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P005-E002'
    AND et.evidence_type_name = 'Behavioral assay / BDA tract tracing'
    AND ot.outcome_type_name = 'Resection outcome after hemisection'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O057', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Abstract-level extraction reports that, in 12-week chronic rat SCI, scar resection was evaluated for locomotor safety and NeuroRegen collagen scaffold plus hUC-MSC implantation into the resected cavity was assessed by locomotion, evoked potentials, and histological repair outcomes.',
    'abstract-level qualitative',
    'Abstract-level extraction reports that, in 12-week chronic rat SCI, scar resection was evaluated for locomotor safety and NeuroRegen collagen scaffold plus hUC-MSC implantation into the resected cavity was assessed by locomotion, evoked potentials, and histological repair outcomes.',
    'chronic resection cavity used as scaffold/cell implantation site',
    'PubMed abstract / Module 1A row',
    'Abstract',
    'low',
    '{"curator_notes": "Full text needed before exact effect sizes or histological endpoints are materialized.", "paper_tracker_id": "M1A-P012", "quantitative": "YES", "statistics_reported": "Abstract-level only", "topic_id": "M1B-T005", "tracker_id": "M1B-O058"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P012-E001–E002'
    AND et.evidence_type_name = 'Behavioral / electrophysiology / histology'
    AND ot.outcome_type_name = 'Scaffold-cell repair after chronic resection'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O058', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In five complete chronic ASIA A SCI patients, SSEP/MEP monitoring was used to distinguish scar from normal neural tissue, scars ranging from 0.5-4.5 cm were resected, and BMMC-loaded NeuroRegen scaffold was implanted into the spinal cord gap.',
    'scar length cm / procedure',
    'In five complete chronic ASIA A SCI patients, SSEP/MEP monitoring was used to distinguish scar from normal neural tissue, scars ranging from 0.5-4.5 cm were resected, and BMMC-loaded NeuroRegen scaffold was implanted into the spinal cord gap.',
    'electrophysiology-guided human scar resection plus scaffold/cell filling',
    'Results / Tables 1-2',
    'Fig 1-Fig 2; Table 1-Table 2',
    'high',
    '{"curator_notes": "MRI lesion length was sometimes smaller than intraoperative electrophysiological scar mapping.", "paper_tracker_id": "M1A-P022", "quantitative": "YES", "statistics_reported": "n = 5 patients; scar length table reported", "topic_id": "M1B-T005", "tracker_id": "M1B-O059"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P022-E001'
    AND et.evidence_type_name = 'Human clinical surgery'
    AND ot.outcome_type_name = 'Scar boundary mapping and gap filling'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O059', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Resected chronic human SCI tissue showed strong CSPG and vimentin staining and negative NF, nestin, Tuj-1, and S100 staining, supporting that the dissected tissue was scar-rich and neural-marker-poor.',
    'marker panel',
    'Resected chronic human SCI tissue showed strong CSPG and vimentin staining and negative NF, nestin, Tuj-1, and S100 staining, supporting that the dissected tissue was scar-rich and neural-marker-poor.',
    'resected human scar is CSPG/vimentin-positive and neural-marker-poor',
    'Results / Figure 3',
    'Fig 3',
    'high',
    '{"curator_notes": "Supports surgical target identity for complete chronic SCI cases.", "paper_tracker_id": "M1A-P022", "quantitative": "YES", "statistics_reported": "qualitative IHC", "topic_id": "M1B-T005", "tracker_id": "M1B-O060"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P022-E002'
    AND et.evidence_type_name = 'Immunohistochemistry'
    AND ot.outcome_type_name = 'Resected human scar composition'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O060', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'After human scar resection and BMMC-loaded NeuroRegen implantation, no obvious adverse effects related to resection or scaffold transplantation were observed immediately or at 12 months; two cases showed lower-limb SSEP recovery by 6 months that persisted to the end of observation.',
    'adverse events / SSEP',
    'After human scar resection and BMMC-loaded NeuroRegen implantation, no obvious adverse effects related to resection or scaffold transplantation were observed immediately or at 12 months; two cases showed lower-limb SSEP recovery by 6 months that persisted to the end of observation.',
    'procedure feasible/safe in small cohort with partial SSEP recovery',
    'Results / Tables 3-4',
    'Table 3-Table 4',
    'high',
    '{"curator_notes": "No neurological deterioration or spine instability was detected after scar resection.", "paper_tracker_id": "M1A-P022", "quantitative": "YES", "statistics_reported": "n = 5; 2 cases with SSEP recovery", "topic_id": "M1B-T005", "tracker_id": "M1B-O061"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P022-E003'
    AND et.evidence_type_name = 'Clinical safety / electrophysiology follow-up'
    AND ot.outcome_type_name = 'Safety and signal recovery'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O061', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Source-page extraction reports that chronic complete SCI scar resection created a cavitary lesion repair setting where decellularized ECM hydrogel scaffold filling, with or without human iPSC-derived NS/PC transplantation, was assessed for histological repair effects.',
    'source-page qualitative',
    'Source-page extraction reports that chronic complete SCI scar resection created a cavitary lesion repair setting where decellularized ECM hydrogel scaffold filling, with or without human iPSC-derived NS/PC transplantation, was assessed for histological repair effects.',
    'dECM scaffold and hNS/PC support after chronic scar resection',
    'Abstract / source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Full text should be parsed for lesion filling, graft survival, and histological outcome details before high-confidence materialization.", "paper_tracker_id": "M1A-P034", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T005", "tracker_id": "M1B-O062"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P034-E001–E002'
    AND et.evidence_type_name = 'Histology / transplantation'
    AND ot.outcome_type_name = 'Scaffold-supported cavitary repair'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O062', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Human SCI lesions changed rapidly from 3 days to 1 month: tissue bridge width increased from 0.68 mm to 1.41 mm, IMLA decreased 75%, and IMLL decreased 73%, then lesion metrics remained largely stable from 1 month to 5 years.',
    'mm / mm2 / percent change',
    'Human SCI lesions changed rapidly from 3 days to 1 month: tissue bridge width increased from 0.68 mm to 1.41 mm, IMLA decreased 75%, and IMLL decreased 73%, then lesion metrics remained largely stable from 1 month to 5 years.',
    'early lesion demarcation then chronic geometry stability',
    'Results / Figure 1',
    'Fig 1',
    'high',
    '{"curator_notes": "Human acute-to-chronic imaging anchor for lesion geometry.", "paper_tracker_id": "M1A-P016", "quantitative": "YES", "statistics_reported": "TB p = 0.02; IMLA/IMLL p < 0.001; stable 1 month-5 years p = 0.28/0.30", "topic_id": "M1B-T007", "tracker_id": "M1B-O063"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P016-E001'
    AND et.evidence_type_name = 'Longitudinal T2 MRI / clinical follow-up'
    AND ot.outcome_type_name = 'Lesion geometry'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O063', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Over 5 years after human SCI, early C1-C3 and intracranial CST swelling with R2* increase and MTsat decrease progressed into C1-C3 and CST volume loss plus continued MTsat/motor-system microstructural changes.',
    'volume / MTsat / R2*',
    'Over 5 years after human SCI, early C1-C3 and intracranial CST swelling with R2* increase and MTsat decrease progressed into C1-C3 and CST volume loss plus continued MTsat/motor-system microstructural changes.',
    'remote motor system shows chronic MRI-visible degeneration',
    'Results / Figure 2',
    'Fig 2',
    'high',
    '{"curator_notes": "Supports chronic lesion effects beyond local epicenter.", "paper_tracker_id": "M1A-P016", "quantitative": "YES", "statistics_reported": "significant FDR-corrected clusters reported", "topic_id": "M1B-T007", "tracker_id": "M1B-O064"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P016-E002'
    AND et.evidence_type_name = 'Quantitative MRI / voxel-based mapping'
    AND ot.outcome_type_name = 'Remote motor-system degeneration'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O064', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Greater first-month tissue bridge increase correlated with motor recovery, while less C1-C3 atrophy, smaller C1-C3 MTsat decrease, less M1/S1 R2* increase, and less swelling related to better motor or SCIM outcomes over 5 years.',
    'correlations / GLM',
    'Greater first-month tissue bridge increase correlated with motor recovery, while less C1-C3 atrophy, smaller C1-C3 MTsat decrease, less M1/S1 R2* increase, and less swelling related to better motor or SCIM outcomes over 5 years.',
    'tissue bridges and remote degeneration metrics predict recovery',
    'Results / Figures 3-4',
    'Fig 3-Fig 4',
    'high',
    '{"curator_notes": "Bridges local lesion geometry to functional outcome.", "paper_tracker_id": "M1A-P016", "quantitative": "YES", "statistics_reported": "TB increase versus motor recovery n = 16, rho = 0.74, p < 0.001; swelling versus motor recovery n = 22, rho = -0.45, p = 0.04", "topic_id": "M1B-T007", "tracker_id": "M1B-O065"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P016-E003'
    AND et.evidence_type_name = 'Association modeling'
    AND ot.outcome_type_name = 'Imaging-recovery linkage'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O065', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In chronic human traumatic SCI cases, large-diameter myelinated ventral-root axons were significantly reduced one level above, at, and one to three levels below the epicenter, indicating motoneuron death and muscle denervation risk.',
    'percent uninjured / axon counts',
    'In chronic human traumatic SCI cases, large-diameter myelinated ventral-root axons were significantly reduced one level above, at, and one to three levels below the epicenter, indicating motoneuron death and muscle denervation risk.',
    'chronic human SCI causes segment-spanning motoneuron loss',
    'Results / Figure 4',
    'Fig 4',
    'high',
    '{"curator_notes": "Cases had chronic SCI >=6 months post-injury.", "paper_tracker_id": "M1A-P019", "quantitative": "YES", "statistics_reported": "E1 51 +/- 14%, E 45 +/- 11%, E-1 27 +/- 12%, E-2 45 +/- 40%, E-3 54 +/- 23% of uninjured; p values reported", "topic_id": "M1B-T007", "tracker_id": "M1B-O066"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P019-E001–E002'
    AND et.evidence_type_name = 'Human post-mortem pathology / ventral-root axon counts'
    AND ot.outcome_type_name = 'Motoneuron loss'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O066', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Large-diameter axons with thin myelin were evident in ventral roots at and below the lesion epicenter; g-ratio increased significantly for large fibers at the epicenter relative to above-lesion roots.',
    'g-ratio',
    'Large-diameter axons with thin myelin were evident in ventral roots at and below the lesion epicenter; g-ratio increased significantly for large fibers at the epicenter relative to above-lesion roots.',
    'incomplete remyelination in chronic human ventral roots',
    'Results / Figure 5',
    'Fig 5',
    'high',
    '{"curator_notes": "Adds myelin pathology to structural lesion profile.", "paper_tracker_id": "M1A-P019", "quantitative": "YES", "statistics_reported": "location p = 0.027; fiber diameter p < 0.001; interaction p < 0.001; large-fiber epicenter p <= 0.003", "topic_id": "M1B-T007", "tracker_id": "M1B-O067"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P019-E003'
    AND et.evidence_type_name = 'Human post-mortem pathology / g-ratio'
    AND ot.outcome_type_name = 'Remyelination abnormality'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O067', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In 19 children with chronic SCI and 36 typically developing controls, both SCIWOMR and MRI-positive groups showed abnormal FA and RD values in adjacent MRI-normal-appearing cephalad and caudal spinal cord segments.',
    'FA / RD',
    'In 19 children with chronic SCI and 36 typically developing controls, both SCIWOMR and MRI-positive groups showed abnormal FA and RD values in adjacent MRI-normal-appearing cephalad and caudal spinal cord segments.',
    'pediatric chronic SCI has DTI abnormalities beyond conventional MRI lesion',
    'Abstract / source page',
    'Abstract / article metadata',
    'medium',
    '{"curator_notes": "Includes traumatic and nontraumatic chronic SCI, >=6 months post-injury.", "paper_tracker_id": "M1A-P028", "quantitative": "YES", "statistics_reported": "Abstract/source-page level; exact values not extracted", "topic_id": "M1B-T007", "tracker_id": "M1B-O068"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P028-E001'
    AND et.evidence_type_name = 'Pediatric spinal cord DTI'
    AND ot.outcome_type_name = 'Normal-appearing cord abnormality'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O068', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In the SCIWOMR subgroup, FA values showed perilesional abnormalities in middle and proximal cephalad and caudal cord segments when AIS A/B children were compared with AIS C/D children.',
    'FA / AIS class',
    'In the SCIWOMR subgroup, FA values showed perilesional abnormalities in middle and proximal cephalad and caudal cord segments when AIS A/B children were compared with AIS C/D children.',
    'DTI perilesional abnormality relates to AIS severity',
    'Abstract / source page',
    'Abstract / article metadata',
    'medium',
    '{"curator_notes": "Useful translational imaging bridge, but full text needed for numeric DTI values.", "paper_tracker_id": "M1A-P028", "quantitative": "YES", "statistics_reported": "Abstract/source-page level; exact values not extracted", "topic_id": "M1B-T007", "tracker_id": "M1B-O069"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P028-E002'
    AND et.evidence_type_name = 'Pediatric spinal cord DTI / clinical severity'
    AND ot.outcome_type_name = 'AIS-linked perilesional abnormality'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O069', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Resected complete chronic SCI scar tissue was CSPG/vimentin-positive and NF/nestin/Tuj-1/S100-negative, providing human tissue evidence for a scar-rich, neural-marker-poor chronic lesion component.',
    'marker panel',
    'Resected complete chronic SCI scar tissue was CSPG/vimentin-positive and NF/nestin/Tuj-1/S100-negative, providing human tissue evidence for a scar-rich, neural-marker-poor chronic lesion component.',
    'human chronic scar component is inhibitory-matrix/stromal-marker rich',
    'Results / Figure 3',
    'Fig 3',
    'high',
    '{"curator_notes": "Duplicates tissue fact from T005 in a human-pathology context.", "paper_tracker_id": "M1A-P022", "quantitative": "YES", "statistics_reported": "qualitative IHC", "topic_id": "M1B-T007", "tracker_id": "M1B-O070"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P022-E002'
    AND et.evidence_type_name = 'Human scar tissue immunohistochemistry'
    AND ot.outcome_type_name = 'Chronic scar marker profile'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O070', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'PLX5622 pre-treatment reduced spinal microglia, infiltrating myeloid cells, monocytes, neutrophils, immune-cell ROS production, CD11b expression, and TNFalpha upregulation at 2 DPI after thoracic contusion.',
    'cell counts / ROS / qPCR',
    'PLX5622 pre-treatment reduced spinal microglia, infiltrating myeloid cells, monocytes, neutrophils, immune-cell ROS production, CD11b expression, and TNFalpha upregulation at 2 DPI after thoracic contusion.',
    'CSF1R inhibition dampens acute lesion-site myeloid inflammation',
    'Results / Figure 1',
    'Fig 1',
    'high',
    '{"curator_notes": "Pre-injury depletion design is a boundary condition.", "paper_tracker_id": "M1A-P006", "quantitative": "YES", "statistics_reported": "figure-level statistics reported; n values per group reported", "topic_id": "M1B-T008", "tracker_id": "M1B-O071"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P006-E001'
    AND et.evidence_type_name = 'Flow cytometry / ROS / qPCR'
    AND ot.outcome_type_name = 'Acute intraspinal inflammation'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O071', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'PLX5622 started after SCI and continued to 7 DPI significantly reduced microglia and infiltrating myeloid counts in the spinal impact site and reduced microglia/myeloid populations in the brain.',
    'cell counts',
    'PLX5622 started after SCI and continued to 7 DPI significantly reduced microglia and infiltrating myeloid counts in the spinal impact site and reduced microglia/myeloid populations in the brain.',
    'post-injury CSF1R inhibition reduces acute spinal and brain myeloid populations',
    'Results / Figure 2',
    'Fig 2',
    'high',
    '{"curator_notes": "Supports myeloid contribution to leukocyte infiltration after injury.", "paper_tracker_id": "M1A-P006", "quantitative": "YES", "statistics_reported": "n = 4-5 per group; p values reported in figure", "topic_id": "M1B-T008", "tracker_id": "M1B-O072"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P006-E002'
    AND et.evidence_type_name = 'Flow cytometry'
    AND ot.outcome_type_name = 'Post-injury myeloid response'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O072', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Long-term post-injury PLX5622 did not significantly improve gross BMS locomotion, but improved CatWalk step-sequence regularity and stride length and improved cognitive/depressive-like behavior readouts at 5-6 WPI.',
    'behavioral scores',
    'Long-term post-injury PLX5622 did not significantly improve gross BMS locomotion, but improved CatWalk step-sequence regularity and stride length and improved cognitive/depressive-like behavior readouts at 5-6 WPI.',
    'microglial depletion improves selected fine motor and brain-linked behavioral outcomes',
    'Results / Figures 3-4',
    'Fig 3-Fig 4',
    'high',
    '{"curator_notes": "Outcome benefit is not a simple gross locomotion/lesion-volume effect.", "paper_tracker_id": "M1A-P006", "quantitative": "YES", "statistics_reported": "regularity p = 0.0056; stride length p = 0.0162; NOR/Y-maze/TS/FS p values reported", "topic_id": "M1B-T008", "tracker_id": "M1B-O073"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P006-E003'
    AND et.evidence_type_name = 'Behavioral testing'
    AND ot.outcome_type_name = 'Neurological recovery'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O073', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'At 6 WPI after severe contusion, PLX5622 reduced CX3CR1-GFP-positive cells by more than 90% but did not significantly change GFAP-positive area, lesion volume, spared white matter, or BMS; it reduced neuronal loss in thalamus and dentate gyrus.',
    'histology / stereology',
    'At 6 WPI after severe contusion, PLX5622 reduced CX3CR1-GFP-positive cells by more than 90% but did not significantly change GFAP-positive area, lesion volume, spared white matter, or BMS; it reduced neuronal loss in thalamus and dentate gyrus.',
    'chronic microglial depletion changes remote neurodegeneration more than lesion volume',
    'Results / Figure 5',
    'Fig 5',
    'high',
    '{"curator_notes": "Important boundary between lesion architecture preservation and remote brain pathology.", "paper_tracker_id": "M1A-P006", "quantitative": "YES", "statistics_reported": "GFP reduction and neuronal-density statistics reported", "topic_id": "M1B-T008", "tracker_id": "M1B-O074"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P006-E005'
    AND et.evidence_type_name = 'Histology / stereology'
    AND ot.outcome_type_name = 'Lesion and remote neurodegeneration'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O074', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'At 6 WPI, spinal cord NanoString showed 384 injury genes; 218 were PLX-modified and nearly all were attenuated, with strongest effects in inflammatory signaling, innate immune response, microglia function, NF-kappaB, cytokine signaling, adaptive immunity, apoptosis, astrocyte function, growth-factor signaling, and matrix remodeling.',
    'differential expression',
    'At 6 WPI, spinal cord NanoString showed 384 injury genes; 218 were PLX-modified and nearly all were attenuated, with strongest effects in inflammatory signaling, innate immune response, microglia function, NF-kappaB, cytokine signaling, adaptive immunity, apoptosis, astrocyte function, growth-factor signaling, and matrix remodeling.',
    'chronic lesion transcriptome has microglia-linked inflammatory/apoptotic/matrix components',
    'Results / Figures 6-9',
    'Fig 6-Fig 9',
    'high',
    '{"curator_notes": "qPCR validated microglial receptors, apoptosis/autophagy markers, and reduced Gfap after PLX.", "paper_tracker_id": "M1A-P006", "quantitative": "YES", "statistics_reported": "adjusted p < 0.05; 218/384 injury genes PLX-modified", "topic_id": "M1B-T008", "tracker_id": "M1B-O075"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P006-E004'
    AND et.evidence_type_name = 'NanoString / qPCR'
    AND ot.outcome_type_name = 'Chronic spinal cord inflammation'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O075', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'SCI altered cortical neuronal/synaptic, apoptosis, and microglia-function genes at 6 WPI; PLX reduced injury-induced Il1a and Lrrc25 and was associated with improved neuronal survival and neurobehavioral outcomes.',
    'differential expression / stereology',
    'SCI altered cortical neuronal/synaptic, apoptosis, and microglia-function genes at 6 WPI; PLX reduced injury-induced Il1a and Lrrc25 and was associated with improved neuronal survival and neurobehavioral outcomes.',
    'chronic SCI-linked brain inflammation is microglia-modifiable',
    'Results / Figures 10-12',
    'Fig 10-Fig 12',
    'high',
    '{"curator_notes": "Extends immune-glial lesion response to remote brain pathology.", "paper_tracker_id": "M1A-P006", "quantitative": "YES", "statistics_reported": "cortex DE genes and qPCR statistics reported", "topic_id": "M1B-T008", "tracker_id": "M1B-O076"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P006-E004–E005'
    AND et.evidence_type_name = 'NanoString / qPCR / brain stereology'
    AND ot.outcome_type_name = 'Remote brain inflammation'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O076', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Source-page extraction reports that injury-activated microglia/macrophages acquire temporal IAM signatures and that myeloid Plexin-B2 deletion disrupts wound corralling, matrix compaction, astrocytic border containment, inflammatory restriction, axon regeneration, and recovery.',
    'source-page qualitative',
    'Source-page extraction reports that injury-activated microglia/macrophages acquire temporal IAM signatures and that myeloid Plexin-B2 deletion disrupts wound corralling, matrix compaction, astrocytic border containment, inflammatory restriction, axon regeneration, and recovery.',
    'myeloid cells can promote lesion containment and compaction',
    'Source page / Module 1A row',
    'Fig 1-Fig 7 / source page',
    'medium',
    '{"curator_notes": "Also supports T003 astrocytic border profile.", "paper_tracker_id": "M1A-P030", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T008", "tracker_id": "M1B-O077"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P030-E001–E002'
    AND et.evidence_type_name = 'Myeloid transcriptomics / conditional deletion'
    AND ot.outcome_type_name = 'Corralling and containment'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O077', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Source-page extraction reports that single-cell RNA-seq resolved injured-spinal-cord scar-like cell heterogeneity and inferred cell-cell interactions shaping the wound-healing/scar environment.',
    'source-page transcriptomic atlas',
    'Source-page extraction reports that single-cell RNA-seq resolved injured-spinal-cord scar-like cell heterogeneity and inferred cell-cell interactions shaping the wound-healing/scar environment.',
    'lesion scar is multicellular immune-glial/stromal interaction ecosystem',
    'Abstract / source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Shared with T001 but placed here for interaction ecology.", "paper_tracker_id": "M1A-P031", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T008", "tracker_id": "M1B-O078"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P031-E001–E002'
    AND et.evidence_type_name = 'scRNA-seq / interaction inference'
    AND ot.outcome_type_name = 'Immune-glial scar ecology'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O078', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Source-page extraction reports that CSF1R inhibition after compression SCI reduced microglia/macrophage proliferation and inflammatory response, promoted tissue preservation, and improved motor recovery.',
    'source-page qualitative',
    'Source-page extraction reports that CSF1R inhibition after compression SCI reduced microglia/macrophage proliferation and inflammatory response, promoted tissue preservation, and improved motor recovery.',
    'CSF1R-pathway modulation can preserve tissue and improve recovery',
    'Abstract / source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Directionally concordant with Li but needs full-text extraction for treatment window and lesion metrics.", "paper_tracker_id": "M1A-P035", "quantitative": "YES", "statistics_reported": "Source-page level in Module 1A", "topic_id": "M1B-T008", "tracker_id": "M1B-O079"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P035-E001–E002'
    AND et.evidence_type_name = 'CSF1R inhibition / recovery'
    AND ot.outcome_type_name = 'Microglia/macrophage modulation'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O079', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In 12 humans with chronic SCI 2-34 years posttrauma, focal cystic atrophy at the impact site replaced a mean longitudinal area of 2.01 +/- 0.60 cm2, less than one spinal cord segment, corresponding to 89.3 +/- 17.4% loss of one-segment longitudinal area.',
    'cm2 / percent one segment',
    'In 12 humans with chronic SCI 2-34 years posttrauma, focal cystic atrophy at the impact site replaced a mean longitudinal area of 2.01 +/- 0.60 cm2, less than one spinal cord segment, corresponding to 89.3 +/- 17.4% loss of one-segment longitudinal area.',
    'chronic human atrophy is focal and cystic at impact site',
    'Abstract / Results / Figure 1',
    'Fig 1; Table 1',
    'high',
    '{"curator_notes": "PDF supplied by user; extracted to data/raw/evidence/M1A-P018.", "paper_tracker_id": "M1A-P018", "quantitative": "YES", "statistics_reported": "quantitative stereology; group summary reported", "topic_id": "M1B-T007", "tracker_id": "M1B-O080"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P018-E001'
    AND et.evidence_type_name = 'MRI stereology'
    AND ot.outcome_type_name = 'Focal cystic atrophy'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O080', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Adjacent spinal cord segments retained substantial area: immediately rostral segments showed 19.4 +/- 7.5% atrophy and caudal segments 16.5 +/- 4.1% atrophy versus normal, leaving about 80.6% rostral and 83.5% caudal area; extensive remote atrophy occurred in 2/12 cases and was attributed to late syrinx formation.',
    'percent atrophy / retained area',
    'Adjacent spinal cord segments retained substantial area: immediately rostral segments showed 19.4 +/- 7.5% atrophy and caudal segments 16.5 +/- 4.1% atrophy versus normal, leaving about 80.6% rostral and 83.5% caudal area; extensive remote atrophy occurred in 2/12 cases and was attributed to late syrinx formation.',
    'adjacent chronic cord mass largely preserved except syrinx cases',
    'Results / Discussion',
    'Fig 2-Fig 3; Table 1',
    'high',
    '{"curator_notes": "Supports bridging short cystic lesion zones plus long remaining parenchyma concept.", "paper_tracker_id": "M1A-P018", "quantitative": "YES", "statistics_reported": "rostral p < 0.05; caudal p < 0.005; 2/12 syrinx cases", "topic_id": "M1B-T007", "tracker_id": "M1B-O081"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P018-E002'
    AND et.evidence_type_name = 'MRI stereology'
    AND ot.outcome_type_name = 'Preserved adjacent cord mass'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O081', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In three uninjured human cervical spinal cords, the sulcal arterial system supplied all anterior gray matter, anterior half of posterior gray matter, approximately inner half of anterior/lateral white columns, and anterior half of posterior white columns, with watershed overlap with pial/posterior spinal artery supply.',
    'qualitative vascular territory',
    'In three uninjured human cervical spinal cords, the sulcal arterial system supplied all anterior gray matter, anterior half of posterior gray matter, approximately inner half of anterior/lateral white columns, and anterior half of posterior white columns, with watershed overlap with pial/posterior spinal artery supply.',
    'human central cord vascular territory mapped to sulcal arterial system',
    'Results / Figures 1-2',
    'Fig 1-Fig 2; Table 2',
    'high',
    '{"curator_notes": "Provides vascular anatomy for interpreting central gray/white matter injury patterns.", "paper_tracker_id": "M1A-P020", "quantitative": "YES", "statistics_reported": "n = 3 uninjured cords; sulcal artery counts reported", "topic_id": "M1B-T007", "tracker_id": "M1B-O082"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P020-E001'
    AND et.evidence_type_name = 'Silicone rubber microangiography'
    AND ot.outcome_type_name = 'Human cord vascular supply'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O082', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Acute human SCI specimens showed severe hemorrhage predominantly in gray matter with surrounding white matter lesions, including decreased staining, disrupted myelin, axonal/periaxonal swelling, and lesions extending far from the injury site; large anterior/posterior/sulcal arteries remained patent, while occluded intramedullary veins were found in degenerated posterior white columns.',
    'histopathology',
    'Acute human SCI specimens showed severe hemorrhage predominantly in gray matter with surrounding white matter lesions, including decreased staining, disrupted myelin, axonal/periaxonal swelling, and lesions extending far from the injury site; large anterior/posterior/sulcal arteries remained patent, while occluded intramedullary veins were found in degenerated posterior white columns.',
    'acute vascular injury produces central hemorrhagic necrosis and remote white matter degeneration without large-artery occlusion',
    'Abstract / Results / Discussion',
    'Fig 3-Fig 5; Table 1',
    'high',
    '{"curator_notes": "Authors implicate sulcal arterial damage and small-vessel/venous obstruction rather than large artery occlusion.", "paper_tracker_id": "M1A-P020", "quantitative": "YES", "statistics_reported": "9 traumatized cords overall; acute cases 20 minutes-18 days", "topic_id": "M1B-T007", "tracker_id": "M1B-O083"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P020-E002'
    AND et.evidence_type_name = 'Human autopsy histopathology'
    AND ot.outcome_type_name = 'Acute vascular lesion pattern'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O083', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In later human SCI specimens 3-9 months postinjury, injured segments showed major tissue loss with large cavitations, while rostral and caudal remote sites showed well-demarcated necrotic infarct-like areas mainly in posterior white columns.',
    'histopathology',
    'In later human SCI specimens 3-9 months postinjury, injured segments showed major tissue loss with large cavitations, while rostral and caudal remote sites showed well-demarcated necrotic infarct-like areas mainly in posterior white columns.',
    'chronic human vascular pathology includes cavitation and remote posterior-column infarcts',
    'Abstract / Results / Discussion',
    'Fig 6-Fig 9; Table 1',
    'high',
    '{"curator_notes": "Adds vascular mechanism context to human chronic lesion architecture.", "paper_tracker_id": "M1A-P020", "quantitative": "YES", "statistics_reported": "chronic/subacute cases up to 9 months", "topic_id": "M1B-T007", "tracker_id": "M1B-O084"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P020-E003'
    AND et.evidence_type_name = 'Human autopsy histopathology'
    AND ot.outcome_type_name = 'Chronic cavitation and remote infarction'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O084', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tetsuya Tamaru; Kazu Kobayakawa; Hirokazu Saiwai; Daijiro Konno; Ken Kijima; Shingo Yoshizaki; Kazuhiro Hata; Hirotaka Iura; Gentaro Ono; Yohei Haruta; Kazuki Kitade; Kei-Ichiro Iida; Ken-Ichi Kawaguchi; Yoshihiro Matsumoto; Kensuke Kubota; Takeshi Maeda; Seiji Okada; Yasuharu Nakashima 2023 M1A-P003-E005 preserves a distinct Mus musculus experiment testing Anti-beta1 integrin antibody after Col-I-SA transplantation with endpoint/readout: After EGFP-positive Col-I-SA transplantation, anti-beta1 integrin antibody was injected at the transplant site; host EGFP-negative/GFAP-positive/N-cadherin-positive astrocyte recruitment was quantified..',
    'qualitative',
    'Tetsuya Tamaru; Kazu Kobayakawa; Hirokazu Saiwai; Daijiro Konno; Ken Kijima; Shingo Yoshizaki; Kazuhiro Hata; Hirotaka Iura; Gentaro Ono; Yohei Haruta; Kazuki Kitade; Kei-Ichiro Iida; Ken-Ichi Kawaguchi; Yoshihiro Matsumoto; Kensuke Kubota; Takeshi Maeda; Seiji Okada; Yasuharu Nakashima 2023 M1A-P003-E005 preserves a distinct Mus musculus experiment testing Anti-beta1 integrin antibody after Col-I-SA transplantation with endpoint/readout: After EGFP-positive Col-I-SA transplantation, anti-beta1 integrin antibody was injected at the transplant site; host EGFP-negative/GFAP-positive/N-cadherin-positive astrocyte recruitment was quantified..',
    'M1A-P003-E005 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Fig 5A-C',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury. Existing consensus links remain on original curated observations.", "paper_tracker_id": "M1A-P003", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M1B-T003", "tracker_id": "M1B-O085"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P003-E005'
    AND et.evidence_type_name = 'In vivo antibody treatment'
    AND ot.outcome_type_name = 'After EGFP-positive Col-I-SA transplantation, anti-beta1 integrin antibody was injected at the transplant site; host EGFP-negative/GFAP-positive/N-cadherin-positive astrocyte recruitment was quantified.'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O085', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tetsuya Tamaru; Kazu Kobayakawa; Hirokazu Saiwai; Daijiro Konno; Ken Kijima; Shingo Yoshizaki; Kazuhiro Hata; Hirotaka Iura; Gentaro Ono; Yohei Haruta; Kazuki Kitade; Kei-Ichiro Iida; Ken-Ichi Kawaguchi; Yoshihiro Matsumoto; Kensuke Kubota; Takeshi Maeda; Seiji Okada; Yasuharu Nakashima 2023 M1A-P003-E006 preserves a distinct Mus musculus experiment testing Anti-beta1 integrin antibody after SCI with endpoint/readout: Anti-beta1 integrin antibody was injected into the spinal cord epicenter every 2 days from 14-26 DPI; GFAP/N-cadherin-positive chronic astrocytes and GAP43-positive area were quantified..',
    'qualitative',
    'Tetsuya Tamaru; Kazu Kobayakawa; Hirokazu Saiwai; Daijiro Konno; Ken Kijima; Shingo Yoshizaki; Kazuhiro Hata; Hirotaka Iura; Gentaro Ono; Yohei Haruta; Kazuki Kitade; Kei-Ichiro Iida; Ken-Ichi Kawaguchi; Yoshihiro Matsumoto; Kensuke Kubota; Takeshi Maeda; Seiji Okada; Yasuharu Nakashima 2023 M1A-P003-E006 preserves a distinct Mus musculus experiment testing Anti-beta1 integrin antibody after SCI with endpoint/readout: Anti-beta1 integrin antibody was injected into the spinal cord epicenter every 2 days from 14-26 DPI; GFAP/N-cadherin-positive chronic astrocytes and GAP43-positive area were quantified..',
    'M1A-P003-E006 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Fig 5D-H',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Glial scar survives until the chronic phase by recruiting scar-forming astrocytes after spinal cord injury. Existing consensus links remain on original curated observations.", "paper_tracker_id": "M1A-P003", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M1B-T006", "tracker_id": "M1B-O086"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P003-E006'
    AND et.evidence_type_name = 'A-layer experiment evidence'
    AND ot.outcome_type_name = 'Anti-beta1 integrin antibody was injected into the spinal cord epicenter every 2 days from 14-26 DPI; GFAP/N-cadherin-positive chronic astrocytes and GAP43-positive area were quantified.'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O086', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Leilei Gong; Yun Gu; Xiaoxiao Han; Chengcheng Luan; Chang Liu; Xinghui Wang; Yufeng Sun; Mengru Zheng; Mengya Fang; Shuhai Yang; Lai Xu; Hualin Sun; Bin Yu; Xiaosong Gu; Songlin Zhou 2023 M1A-P004-E003 preserves a distinct Mus musculus experiment testing Scar gene-network maturation with endpoint/readout: WGCNA and co-expression module analyses identified time-correlated scar modules, including ECM-receptor and lysosome-associated modules..',
    'qualitative',
    'Leilei Gong; Yun Gu; Xiaoxiao Han; Chengcheng Luan; Chang Liu; Xinghui Wang; Yufeng Sun; Mengru Zheng; Mengya Fang; Shuhai Yang; Lai Xu; Hualin Sun; Bin Yu; Xiaosong Gu; Songlin Zhou 2023 M1A-P004-E003 preserves a distinct Mus musculus experiment testing Scar gene-network maturation with endpoint/readout: WGCNA and co-expression module analyses identified time-correlated scar modules, including ECM-receptor and lysosome-associated modules..',
    'M1A-P004-E003 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Fig 9A-H',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Spatiotemporal Dynamics of the Molecular Expression Pattern and Intercellular Interactions in the Glial Scar Response to Spinal Cord Injury. Existing consensus links remain on original curated observations.", "paper_tracker_id": "M1A-P004", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M1B-T001", "tracker_id": "M1B-O087"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P004-E003'
    AND et.evidence_type_name = 'WGCNA / phase synthesis'
    AND ot.outcome_type_name = 'WGCNA and co-expression module analyses identified time-correlated scar modules, including ECM-receptor and lysosome-associated modules.'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O087', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'John G. Cooper; Su Ji Jeong; Tammy L. McGuire; Sripadh Sharma; Wenxia Wang; Swati Bhattacharyya; John Varga; John A. Kessler 2018 M1A-P007-E004 preserves a distinct Mus musculus experiment testing FnEDA domain deletion with endpoint/readout: 20 um mid-sagittal sections stained for SMI-312; axonal staining intensity quantified across distances from lesion center and normalized to 2 mm rostral tissue..',
    'qualitative',
    'John G. Cooper; Su Ji Jeong; Tammy L. McGuire; Sripadh Sharma; Wenxia Wang; Swati Bhattacharyya; John Varga; John A. Kessler 2018 M1A-P007-E004 preserves a distinct Mus musculus experiment testing FnEDA domain deletion with endpoint/readout: 20 um mid-sagittal sections stained for SMI-312; axonal staining intensity quantified across distances from lesion center and normalized to 2 mm rostral tissue..',
    'M1A-P007-E004 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Fig 4A-C',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Fibronectin EDA forms the chronic fibrotic scar after contusive spinal cord injury. Existing consensus links remain on original curated observations.", "paper_tracker_id": "M1A-P007", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M1B-T001", "tracker_id": "M1B-O088"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P007-E004'
    AND et.evidence_type_name = 'Axon staining / behavior'
    AND ot.outcome_type_name = '20 um mid-sagittal sections stained for SMI-312; axonal staining intensity quantified across distances from lesion center and normalized to 2 mm rostral tissue.'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O088', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'John G. Cooper; Su Ji Jeong; Tammy L. McGuire; Sripadh Sharma; Wenxia Wang; Swati Bhattacharyya; John Varga; John A. Kessler 2018 M1A-P007-E005 preserves a distinct Mus musculus experiment testing FnEDA domain deletion with endpoint/readout: Blinded open-field locomotor scoring using BMS and modified BBB; mice with combined 24 h BMS >1 excluded as improperly injured..',
    'qualitative',
    'John G. Cooper; Su Ji Jeong; Tammy L. McGuire; Sripadh Sharma; Wenxia Wang; Swati Bhattacharyya; John Varga; John A. Kessler 2018 M1A-P007-E005 preserves a distinct Mus musculus experiment testing FnEDA domain deletion with endpoint/readout: Blinded open-field locomotor scoring using BMS and modified BBB; mice with combined 24 h BMS >1 excluded as improperly injured..',
    'M1A-P007-E005 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Fig 5A-D',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Fibronectin EDA forms the chronic fibrotic scar after contusive spinal cord injury. Existing consensus links remain on original curated observations.", "paper_tracker_id": "M1A-P007", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M1B-T001", "tracker_id": "M1B-O089"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P007-E005'
    AND et.evidence_type_name = 'A-layer experiment evidence'
    AND ot.outcome_type_name = 'Blinded open-field locomotor scoring using BMS and modified BBB; mice with combined 24 h BMS >1 excluded as improperly injured.'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O089', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Robert M Grumbles; Christine K Thomas 2017 M1A-P019-E001 preserves a distinct Homo sapiens experiment testing Post-mortem tissue-bank pathology with endpoint/readout: Human ventral roots and cord sections were classified by lesion level and injury type; solochrome cyanine/Sevier-Munger cord pathology and toluidine blue ventral-root histology established tissue context and sampling..',
    'qualitative',
    'Robert M Grumbles; Christine K Thomas 2017 M1A-P019-E001 preserves a distinct Homo sapiens experiment testing Post-mortem tissue-bank pathology with endpoint/readout: Human ventral roots and cord sections were classified by lesion level and injury type; solochrome cyanine/Sevier-Munger cord pathology and toluidine blue ventral-root histology established tissue context and sampling..',
    'M1A-P019-E001 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Table 1; Fig 1-Fig 3',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Motoneuron Death after Human Spinal Cord Injury. Existing consensus links remain on original curated observations.", "paper_tracker_id": "M1A-P019", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M1B-T007", "tracker_id": "M1B-O090"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P019-E001'
    AND et.evidence_type_name = 'Human post-mortem pathology / ventral-root axon counts'
    AND ot.outcome_type_name = 'Human ventral roots and cord sections were classified by lesion level and injury type; solochrome cyanine/Sevier-Munger cord pathology and toluidine blue ventral-root histology established tissue context and sampling.'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O090', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Robert M Grumbles; Christine K Thomas 2017 M1A-P019-E002 preserves a distinct Homo sapiens experiment testing Motoneuron death estimation from ventral-root axons with endpoint/readout: Large-diameter myelinated axons (>=7 um) were sampled and counted in ventral roots above, at, and below the lesion epicenter to estimate motoneuron loss relative to uninjured controls..',
    'qualitative',
    'Robert M Grumbles; Christine K Thomas 2017 M1A-P019-E002 preserves a distinct Homo sapiens experiment testing Motoneuron death estimation from ventral-root axons with endpoint/readout: Large-diameter myelinated axons (>=7 um) were sampled and counted in ventral roots above, at, and below the lesion epicenter to estimate motoneuron loss relative to uninjured controls..',
    'M1A-P019-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Fig 4',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Motoneuron Death after Human Spinal Cord Injury. Existing consensus links remain on original curated observations.", "paper_tracker_id": "M1A-P019", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M1B-T003", "tracker_id": "M1B-O091"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P019-E002'
    AND et.evidence_type_name = 'A-layer experiment evidence'
    AND ot.outcome_type_name = 'Large-diameter myelinated axons (>=7 um) were sampled and counted in ventral roots above, at, and below the lesion epicenter to estimate motoneuron loss relative to uninjured controls.'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O091', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'F Scholtes; E Theunissen; R Phan-Ba; P Adriaensens; G Brook; R Franzen; J Gelan; J Schoenen; D Martin 2011 M1A-P024-E001 preserves a distinct Rattus norvegicus experiment testing Post-mortem 9.4 T MRI with endpoint/readout: Five excised rat spines were imaged post-mortem using high-resolution proton density MRI with inversion recovery to depict lesion volume, cord atrophy, and spared white matter..',
    'qualitative',
    'F Scholtes; E Theunissen; R Phan-Ba; P Adriaensens; G Brook; R Franzen; J Gelan; J Schoenen; D Martin 2011 M1A-P024-E001 preserves a distinct Rattus norvegicus experiment testing Post-mortem 9.4 T MRI with endpoint/readout: Five excised rat spines were imaged post-mortem using high-resolution proton density MRI with inversion recovery to depict lesion volume, cord atrophy, and spared white matter..',
    'M1A-P024-E001 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract methods/results; figures on Nature page',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Post-mortem assessment of rat spinal cord injury and white matter sparing using inversion recovery-supported proton density magnetic resonance imaging. Existing consensus links remain on original curated observations.", "paper_tracker_id": "M1A-P024", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M1B-T006", "tracker_id": "M1B-O092"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P024-E001'
    AND et.evidence_type_name = 'Post-mortem MRI / histology / BBB'
    AND ot.outcome_type_name = 'Five excised rat spines were imaged post-mortem using high-resolution proton density MRI with inversion recovery to depict lesion volume, cord atrophy, and spared white matter.'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O092', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'F Scholtes; E Theunissen; R Phan-Ba; P Adriaensens; G Brook; R Franzen; J Gelan; J Schoenen; D Martin 2011 M1A-P024-E002 preserves a distinct Rattus norvegicus experiment testing MRI-histology-functional validation with endpoint/readout: Weekly BBB locomotor recovery was compared with MRI lesion severity and white matter sparing, and histology was used to confirm MRI interpretation..',
    'qualitative',
    'F Scholtes; E Theunissen; R Phan-Ba; P Adriaensens; G Brook; R Franzen; J Gelan; J Schoenen; D Martin 2011 M1A-P024-E002 preserves a distinct Rattus norvegicus experiment testing MRI-histology-functional validation with endpoint/readout: Weekly BBB locomotor recovery was compared with MRI lesion severity and white matter sparing, and histology was used to confirm MRI interpretation..',
    'M1A-P024-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract methods/results; figures on Nature page',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Post-mortem assessment of rat spinal cord injury and white matter sparing using inversion recovery-supported proton density magnetic resonance imaging. Existing consensus links remain on original curated observations.", "paper_tracker_id": "M1A-P024", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M1B-T005", "tracker_id": "M1B-O093"}'
  FROM _m1_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M1A-P024-E002'
    AND et.evidence_type_name = 'A-layer experiment evidence'
    AND ot.outcome_type_name = 'Weekly BBB locomotor recovery was compared with MRI lesion severity and white matter sparing, and histology was used to confirm MRI interpretation.'
  RETURNING observation_id
)
INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT 'M1B-O093', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic rat hemisection SCI scar has decreased Young''s modulus, and scar softening is associated with cavitation, CNS cell loss/dysregulation, dense nuclei packing, and GAG/HA dysregulation.',
    'conclusion',
    'high',
    'Abstract / Conclusion',
    'high',
    '{"curator_notes": "Claim is directly aligned with Fig 1-Fig 4 observations.", "topic_id": "M1B-T004", "tracker_id": "M1B-C001"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P026'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Differences between chronic scar mechanics studies likely depend on injury model, time point, sample preparation, and AFM methodology.',
    'interpretation',
    'medium',
    'Introduction / Discussion',
    'high',
    '{"curator_notes": "Boundary-condition claim explicitly discusses Cooper 2020 versus Baumann 2020.", "topic_id": "M1B-T004", "tracker_id": "M1B-C002"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P026'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic severe mouse contusion SCI produces mechanical stiffening of spinal lesion tissue compared with uninjured tissue.',
    'conclusion',
    'high',
    'Abstract / Discussion',
    'high',
    '{"curator_notes": "Directly supported by AFM lesion measurements.", "topic_id": "M1B-T004", "tracker_id": "M1B-C003"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P027'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Fibrotic scarring is a key driver of chronic mechanical stiffening after SCI, because immune-modifying nanoparticle treatment reduces fibrotic scarring and rescues lesion stiffness.',
    'mechanistic',
    'medium',
    'Abstract / Discussion',
    'high',
    '{"curator_notes": "Supported by IMP intervention but still mechanistic because IMP has immune and scar effects.", "topic_id": "M1B-T004", "tracker_id": "M1B-C004"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P027'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic lesion stiffness is biologically relevant because mouse and human astrocytes respond to substrate stiffness values in the injured/uninjured spinal cord range.',
    'implication',
    'medium',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Supported by in vitro substrate observations; extrapolation to in vivo phenotype remains interpretive.", "topic_id": "M1B-T004", "tracker_id": "M1B-C005"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P027'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'In contusive SCI with largely intact dura, Col1alpha1-positive perivascular fibroblasts are a major source of the fibrotic scar and are distinct from NG2-positive pericytes.',
    'conclusion',
    'high',
    'Abstract / Discussion / Conclusion',
    'high',
    '{"curator_notes": "Strongly supported by Col1alpha1-GFP mapping, immunophenotyping, LSFM, and NG2 lineage tracing.", "topic_id": "M1B-T002", "tracker_id": "M1B-C006"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P008'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Fibrotic scar origin and geometry differ with injury type because penetrating injuries that disrupt dura can add meningeal continuity not seen in closed-dura contusion.',
    'interpretation',
    'medium',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Supported by dorsal hemisection versus contusion comparison.", "topic_id": "M1B-T002", "tracker_id": "M1B-C007"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P008'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Type A pericyte-derived stromal cells are required for fibrotic scar tissue generation and broad injury-induced ECM/fibrosis gene expression after SCI.',
    'mechanistic',
    'high',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Supported by Glast-Rasless attenuation, histology, RNA-seq, qPCR/protein validation.", "topic_id": "M1B-T002", "tracker_id": "M1B-C008"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P009'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Moderate attenuation of pericyte-derived fibrotic scarring promotes CST and raphespinal axon regeneration, circuit integration, and sensorimotor recovery after SCI.',
    'conclusion',
    'high',
    'Abstract / Results / Conclusion',
    'high',
    '{"curator_notes": "Supported across tracing, optogenetics, electrophysiology, behavior, and correlation analyses.", "topic_id": "M1B-T002", "tracker_id": "M1B-C009"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P009'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Complete blockade of fibrotic scar formation is harmful because the fibrotic response is needed for tissue closure; the therapeutic window is partial attenuation rather than ablation.',
    'interpretation',
    'medium',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Based on Tam-def animals with tissue defects and poor regeneration/recovery.", "topic_id": "M1B-T002", "tracker_id": "M1B-C010"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P009'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Fibrotic scars after transection and crush SCI primarily derive from perivascular and meningeal fibroblasts rather than pericytes/vSMCs in the authors'' lineage-tracing system.',
    'conclusion',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Directly boundary-checks the pericyte-origin model using Myh11, NG2, Col1a2, and Crabp2 lineage tools.", "topic_id": "M1B-T002", "tracker_id": "M1B-C011"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P021'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Fibrotic scar tissue is heterogeneous: central CE-F and peripheral/perivascular LA-F occupy distinct scar regions and have different ECM, lipid, and angiogenesis-associated programs.',
    'conclusion',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Supported in mouse and monkey datasets plus functional assays.", "topic_id": "M1B-T002", "tracker_id": "M1B-C012"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P021'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'The glial scar persists into the chronic phase through scar-forming astrocytes that maintain a robust N-cadherin-associated phenotype while changing some gene-expression features over time.',
    'conclusion',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Supported by contusion time course, LMD-qPCR, and chronic 12 WPI analysis.", "topic_id": "M1B-T003", "tracker_id": "M1B-C013"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Established scar-forming astrocytes are not readily reverted by removing collagen signaling or blocking beta1-integrin/N-cadherin in vitro, but beta1-integrin blockade can reduce recruitment of new scar-forming astrocytes in vivo.',
    'mechanistic',
    'high',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Important distinction between state maintenance and recruitment.", "topic_id": "M1B-T003", "tracker_id": "M1B-C014"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Reducing beta1-integrin-dependent recruitment of chronic scar-forming astrocytes can shrink the glial scar and promote axonal regeneration markers after SCI.',
    'implication',
    'medium',
    'Results / Discussion',
    'high',
    '{"curator_notes": "GAP43-positive area is a regeneration-associated marker, not a full functional recovery endpoint.", "topic_id": "M1B-T003", "tracker_id": "M1B-C015"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P003'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injury-activated microglia/macrophages promote corralling, wound compaction, astrocytic border containment, and recovery through Plexin-B2.',
    'mechanistic',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Source-page level; full-text extraction still needed.", "topic_id": "M1B-T003", "tracker_id": "M1B-C016"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P030'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Astrocytic Ryk signaling coordinates astrocyte morphological transformation, scarring, wound healing, and lesion-core containment after SCI.',
    'mechanistic',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Source-page level; full-text extraction still needed.", "topic_id": "M1B-T003", "tracker_id": "M1B-C017"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P032'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Border-forming wound repair astrocytes are an active, transcriptionally reprogrammed repair state derived mainly from local astrocytes with a minority OPC-derived contribution.',
    'conclusion',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Source-page level; full-text extraction still needed.", "topic_id": "M1B-T003", "tracker_id": "M1B-C018"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P033'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'SCI scar architecture is spatially heterogeneous and multicellular, with fibroblast-rich central regions, microglial/astrocytic boundary layers, endothelial/oligodendrocyte-associated compartments, and time-dependent maturation.',
    'conclusion',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Supported by spatial transcriptomic atlas, marker maps, and cell-fraction analyses.", "topic_id": "M1B-T001", "tracker_id": "M1B-C019"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P004'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Scar formation follows a staged process in the lateral hemisection model: macrophage infiltration, proliferation/differentiation of scar-resident cells, scar emergence, and stationary scar.',
    'interpretation',
    'medium',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Author synthesis from ST time course; should be model-specific.", "topic_id": "M1B-T001", "tracker_id": "M1B-C020"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P004'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'FnEDA is required for long-term stability of the assembled fibronectin matrix and for the chronic fibrotic scar after contusive SCI, without being required for acute fibrotic response or GFAP glial scarring.',
    'mechanistic',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Strongly supported by FnEDA-null matrix fractionation and chronic lesion histology.", "topic_id": "M1B-T001", "tracker_id": "M1B-C021"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P007'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Reducing chronic FnEDA-dependent fibrotic scarring improves axonal density and locomotor recovery after contusive SCI.',
    'implication',
    'medium',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Supported by genotype comparison; causal inference should stay tied to FnEDA-null model.", "topic_id": "M1B-T001", "tracker_id": "M1B-C022"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P007'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic contusion repair tissue can be described as fibrotic, cellular, and axonal zones, and combined scar ablation/transplantation can alter zone integration and cavity morphology.',
    'conclusion',
    'low',
    'Abstract',
    'medium',
    '{"curator_notes": "Abstract-level only; useful as historical/zone-architecture support.", "topic_id": "M1B-T001", "tracker_id": "M1B-C023"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P001'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'The injured spinal cord scar environment is a heterogeneous multicellular ecosystem whose cell-cell interactions shape wound healing and inhibitory scar features.',
    'conclusion',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Source-page level; full text still needed.", "topic_id": "M1B-T001", "tracker_id": "M1B-C024"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P031'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Spared lesion-remote white matter is an active repair compartment where region-specific astrocyte states regulate debris-clearing microglia and neurological recovery after SCI.',
    'conclusion',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Strongly supported by transcriptomics, spatial mapping, conditional deletion, debris assays, and behavior.", "topic_id": "M1B-T006", "tracker_id": "M1B-C025"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P014'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C025', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Astrocyte-derived CCN1 coordinates white matter repair by restricting excessive microglial activation and supporting lipid/debris processing in Wallerian-degenerating tracts.',
    'mechanistic',
    'high',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Supported by Ccn1-cKO, CCN1 protein/secreted factor, debris, and lipid assays.", "topic_id": "M1B-T006", "tracker_id": "M1B-C026"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P014'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C026', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'White matter sparing can be detected by high-resolution MRI and aligns with histology and locomotor recovery after chronic rat SCI.',
    'conclusion',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Source-page/abstract-level details; n = 5.", "topic_id": "M1B-T006", "tracker_id": "M1B-C027"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P024'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C027', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'In vivo MRI can track white matter tract pathology after severe thoracic SCI and relate spared white matter to hindlimb recovery.',
    'conclusion',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Needs full-text metric extraction.", "topic_id": "M1B-T006", "tracker_id": "M1B-C028"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P036'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C028', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Residual white matter undergoes chronic cellular-composition changes after contusion SCI, making spared funiculi a lesion-adjacent compartment rather than normal tissue.',
    'conclusion',
    'low',
    'Abstract',
    'medium',
    '{"curator_notes": "Abstract-level only.", "topic_id": "M1B-T006", "tracker_id": "M1B-C029"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P013'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C029', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Glial scar resection alone is not uniformly beneficial after SCI; it can be neutral after dorsal hemisection and harmful after contusion, implying that the scar can have protective/stabilizing functions.',
    'interpretation',
    'high',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Strong boundary-condition claim for scaffold/resection strategies.", "topic_id": "M1B-T005", "tracker_id": "M1B-C030"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P005'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C030', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic scar resection can be used as a preparation step for NeuroRegen collagen scaffold plus hUC-MSC implantation, with outcomes assessed by locomotion, electrophysiology, and histological repair.',
    'conclusion',
    'low',
    'Abstract',
    'medium',
    '{"curator_notes": "Abstract-level only until full text is parsed.", "topic_id": "M1B-T005", "tracker_id": "M1B-C031"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P012'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C031', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'In complete chronic SCI patients, electrophysiology-guided scar resection followed by BMMC-loaded NeuroRegen scaffold implantation is feasible and did not produce obvious procedure-related adverse effects in a small one-year cohort.',
    'conclusion',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Keep scoped to five ASIA A patients and feasibility/safety, not proven efficacy.", "topic_id": "M1B-T005", "tracker_id": "M1B-C032"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P022'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C032', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human chronic resection specimens can be scar-rich and neural-marker-poor, supporting careful scar targeting in complete chronic cases but highlighting a challenge for incomplete injuries where scar and spared neural tissue may mix.',
    'interpretation',
    'medium',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Directly tied to CSPG/vimentin-positive and neural-marker-negative specimen plus authors'' incomplete-injury caution.", "topic_id": "M1B-T005", "tracker_id": "M1B-C033"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P022'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C033', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Scaffold-supported filling of chronic post-resection cavitary lesions, including dECM hydrogel with human iPSC-derived NS/PCs, is a recurring histological repair strategy in chronic complete SCI models.',
    'conclusion',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Source-page level; exact histological endpoints need full-text extraction.", "topic_id": "M1B-T005", "tracker_id": "M1B-C034"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P034'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C034', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human spinal lesion geometry undergoes rapid early demarcation, then remains relatively stable from 1 month to at least 5 years, while remote motor-system degeneration continues and relates to recovery.',
    'conclusion',
    'high',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Strong longitudinal MRI evidence.", "topic_id": "M1B-T007", "tracker_id": "M1B-C035"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P016'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C035', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Midsagittal tissue bridges and remote MRI metrics are clinically meaningful human lesion-architecture variables because they associate with motor and functional recovery over 5 years.',
    'interpretation',
    'high',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Author interpretation supported by correlations and GLMs.", "topic_id": "M1B-T007", "tracker_id": "M1B-C036"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P016'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C036', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic human SCI produces segment-spanning motoneuron loss and muscle denervation risk, measurable as reduced large-diameter myelinated axons in ventral roots around the lesion.',
    'conclusion',
    'high',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Direct post-mortem pathology evidence.", "topic_id": "M1B-T007", "tracker_id": "M1B-C037"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P019'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C037', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Thin myelin on large ventral-root axons at or below the epicenter indicates incomplete remyelination as a chronic human SCI pathology feature.',
    'conclusion',
    'high',
    'Results / Discussion',
    'high',
    '{"curator_notes": "Directly supported by g-ratio analysis.", "topic_id": "M1B-T007", "tracker_id": "M1B-C038"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P019'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C038', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Pediatric chronic SCI can show DTI abnormalities in adjacent MRI-normal-appearing cord, and FA abnormalities can relate to AIS severity even when conventional MRI is normal.',
    'conclusion',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Source-page/abstract-level until full text values are parsed.", "topic_id": "M1B-T007", "tracker_id": "M1B-C039"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P028'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C039', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human chronic complete SCI scar tissue can be CSPG/vimentin-positive and neural-marker-poor, providing tissue-level support for a persistent scar-rich component in chronic lesions.',
    'conclusion',
    'high',
    'Results / Figure 3',
    'high',
    '{"curator_notes": "Same tissue observation also supports T005 scar-resection boundary.", "topic_id": "M1B-T007", "tracker_id": "M1B-C040"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P022'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C040', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CSF1R inhibition with PLX5622 reduces acute spinal cord microglia/myeloid infiltration, ROS, and inflammatory cytokine expression after contusion SCI.',
    'conclusion',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Supported by pre- and post-injury treatment experiments.", "topic_id": "M1B-T008", "tracker_id": "M1B-C041"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P006'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C041', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic microglia-linked neuroinflammation after SCI modifies spinal cord and brain transcriptomes, astrocyte/matrix/apoptosis programs, remote neuronal survival, and selected neurological behaviors.',
    'conclusion',
    'high',
    'Results / Discussion / Conclusion',
    'high',
    '{"curator_notes": "Captures spinal and remote brain components without claiming reduced lesion volume.", "topic_id": "M1B-T008", "tracker_id": "M1B-C042"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P006'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C042', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Beneficial immune modulation is timing- and function-dependent because early microglia may support neuroprotection/repair, while sustained neurotoxic activation contributes to chronic pathology.',
    'interpretation',
    'medium',
    'Discussion',
    'high',
    '{"curator_notes": "Explicit author discussion; important boundary for T008 consensus.", "topic_id": "M1B-T008", "tracker_id": "M1B-C043"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P006'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C043', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injury-activated microglia/macrophages can be required for lesion corralling, wound compaction, astrocytic containment, inflammatory restriction, axon regeneration, and recovery through Plexin-B2.',
    'mechanistic',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Source-page level; full-text extraction needed before high-confidence materialization.", "topic_id": "M1B-T008", "tracker_id": "M1B-C044"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P030'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C044', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'The injured spinal cord scar environment is a multicellular interaction ecosystem whose immune, glial, and stromal cell states communicate during wound healing and scar formation.',
    'conclusion',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Shared conceptual bridge with T001.", "topic_id": "M1B-T008", "tracker_id": "M1B-C045"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P031'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C045', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CSF1R-pathway inhibition can reduce microglia/macrophage proliferation and inflammation while promoting tissue preservation and motor recovery after SCI.',
    'conclusion',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Source-page level; treatment timing/details needed.", "topic_id": "M1B-T008", "tracker_id": "M1B-C046"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P035'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C046', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic human traumatic SCI usually preserves substantial spinal cord mass adjacent to a relatively short focal cystic atrophy zone, with extensive remote atrophy mainly occurring when late syrinx formation develops.',
    'conclusion',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Full text supplied by user.", "topic_id": "M1B-T007", "tracker_id": "M1B-C047"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P018'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C047', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Neural repair strategies in chronic human SCI should account for bridging short cystic atrophy zones while supporting axonal growth through longer remaining cord parenchyma.',
    'implication',
    'medium',
    'Abstract / Discussion',
    'high',
    '{"curator_notes": "Translational interpretation; not a direct therapeutic experiment.", "topic_id": "M1B-T007", "tracker_id": "M1B-C048"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P018'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C048', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human SCI vascular pathology is centered on sulcal-artery/small-vessel territory damage, gray-matter hemorrhagic necrosis, surrounding white-matter degeneration, and later central myelomalacia/cavitation rather than complete occlusion of major spinal arteries.',
    'mechanistic',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Full text supplied by user.", "topic_id": "M1B-T007", "tracker_id": "M1B-C049"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P020'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C049', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remote rostral and caudal white-matter necrosis/infarction, especially in posterior columns, is part of human SCI vascular pathology and should be represented separately from local impact-site cavitation.',
    'conclusion',
    'high',
    'Abstract / Results / Discussion',
    'high',
    '{"curator_notes": "Supports separate local and remote pathology fields.", "topic_id": "M1B-T007", "tracker_id": "M1B-C050"}'
  FROM _m1_paper_map p
  WHERE p.tracker_id = 'M1A-P020'
  RETURNING claim_id
)
INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT 'M1B-C050', claim_id FROM inserted;

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "AFM evidence for chronic hemisection scar softening.", "tracker_id": "M1B-L001"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O001'
WHERE c.tracker_id = 'M1B-C001';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Cavitation and dense nuclei organization are proposed contributors to softening.", "tracker_id": "M1B-L002"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O002'
WHERE c.tracker_id = 'M1B-C001';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "CNS marker loss/dysregulation and vimentin upregulation support altered cell composition.", "tracker_id": "M1B-L003"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O003'
WHERE c.tracker_id = 'M1B-C001';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "sGAG/CSPG changes support ECM dysregulation.", "tracker_id": "M1B-L004"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O004'
WHERE c.tracker_id = 'M1B-C001';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "HA upregulation supports GAG/HA dysregulation.", "tracker_id": "M1B-L005"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O005'
WHERE c.tracker_id = 'M1B-C001';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Baumann uses fresh 500 um rat hemisection tissue and reports softening.", "tracker_id": "M1B-L006"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O001'
WHERE c.tracker_id = 'M1B-C002';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Cooper validates freeze/thaw method in mouse spinal cord.", "tracker_id": "M1B-L007"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O006'
WHERE c.tracker_id = 'M1B-C002';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Cooper uses chronic mouse contusion and reports stiffening.", "tracker_id": "M1B-L008"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O007'
WHERE c.tracker_id = 'M1B-C002';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "AFM observation supports chronic contusion stiffening.", "tracker_id": "M1B-L009"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O007'
WHERE c.tracker_id = 'M1B-C003';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contradicts',
  '{"notes": "Baumann''s chronic rat hemisection AFM direction differs from Cooper''s chronic mouse contusion direction.", "tracker_id": "M1B-L010"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O001'
WHERE c.tracker_id = 'M1B-C003';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "IMP reduces lesion stiffness from saline-treated injury levels.", "tracker_id": "M1B-L011"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O009'
WHERE c.tracker_id = 'M1B-C004';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "IMP changes glial/fibrotic interface alignment; supports scar-architecture effect but not fibrosis alone.", "tracker_id": "M1B-L012"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O011'
WHERE c.tracker_id = 'M1B-C004';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Human and mouse astrocyte substrate response supports mechanosensitivity claim.", "tracker_id": "M1B-L013"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O008'
WHERE c.tracker_id = 'M1B-C005';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Baseline Col1alpha1-positive cells match a perivascular fibroblast-like profile rather than NG2/nestin pericyte profile.", "tracker_id": "M1B-L014"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O012'
WHERE c.tracker_id = 'M1B-C006';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Col1alpha1-positive cells accumulate into the contusion fibrotic scar and form the GFAP-apposed scar region.", "tracker_id": "M1B-L015"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O013'
WHERE c.tracker_id = 'M1B-C006';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Injured Col1alpha1-positive scar cells remain PDGFRbeta-positive while excluding nonfibroblast markers.", "tracker_id": "M1B-L016"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O014'
WHERE c.tracker_id = 'M1B-C006';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "NG2 lineage tracing shows little overlap with Col1alpha1-positive scar cells.", "tracker_id": "M1B-L017"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O016'
WHERE c.tracker_id = 'M1B-C006';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Dorsal hemisection produces dura-continuous Col1alpha1 scar geometry distinct from contusion.", "tracker_id": "M1B-L018"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O015'
WHERE c.tracker_id = 'M1B-C007';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Contusion scar timing and GFAP border organization provide the comparison point for injury-model geometry.", "tracker_id": "M1B-L019"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O013'
WHERE c.tracker_id = 'M1B-C007';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Glast-Rasless attenuation reduces PDGFRbeta-positive stromal scar occupancy.", "tracker_id": "M1B-L020"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O017'
WHERE c.tracker_id = 'M1B-C008';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "RNA-seq and fibrosis-associated gene changes support dependence of ECM/fibrosis program on type A pericyte progeny.", "tracker_id": "M1B-L021"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O018'
WHERE c.tracker_id = 'M1B-C008';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Scar attenuation permits CST axon growth into or beyond lesion regions at chronic time points.", "tracker_id": "M1B-L022"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O019'
WHERE c.tracker_id = 'M1B-C009';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Optogenetic/electrophysiology evidence supports caudal circuit integration.", "tracker_id": "M1B-L023"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O020'
WHERE c.tracker_id = 'M1B-C009';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Behavioral recovery and axon-count correlations support functional relevance.", "tracker_id": "M1B-L024"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O021'
WHERE c.tracker_id = 'M1B-C009';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Tam-def animals show tissue defects when scar formation is completely blocked.", "tracker_id": "M1B-L025"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O017'
WHERE c.tracker_id = 'M1B-C010';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Tissue-defect animals do not show the same regeneration benefit as partial-attenuation animals.", "tracker_id": "M1B-L026"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O019'
WHERE c.tracker_id = 'M1B-C010';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "PDGFRbeta-lineage recruitment establishes scar-forming perivascular/meningeal pool but not fibroblast specificity alone.", "tracker_id": "M1B-L027"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O022'
WHERE c.tracker_id = 'M1B-C011';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "scRNA-seq and lineage tracing support fibroblast origin and little Myh11/NG2 pericyte/vSMC contribution.", "tracker_id": "M1B-L028"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O023'
WHERE c.tracker_id = 'M1B-C011';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'concordant_boundary',
  '{"notes": "Soderblom''s NG2 tracing is directionally consistent with Xue''s limited NG2 contribution, though marker systems differ.", "tracker_id": "M1B-L029"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O016'
WHERE c.tracker_id = 'M1B-C011';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contradicts',
  '{"notes": "Dias''s type A pericyte-derived scar attenuation claim conflicts with Xue''s interpretation that GLAST-positive scar-forming cells are fibroblasts/PFs rather than pericytes/vSMCs.", "tracker_id": "M1B-L030"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O017'
WHERE c.tracker_id = 'M1B-C011';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "CE-F and LA-F spatial compartment mapping supports heterogeneous scar organization.", "tracker_id": "M1B-L031"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O024'
WHERE c.tracker_id = 'M1B-C012';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Monkey lesion profiling supports cross-species relevance of fibroblast subtype organization.", "tracker_id": "M1B-L032"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O025'
WHERE c.tracker_id = 'M1B-C012';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Functional assays support distinct CE-F and LA-F roles in ECM, lipid, and angiogenesis programs.", "tracker_id": "M1B-L033"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O026'
WHERE c.tracker_id = 'M1B-C012';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Chronic 12 WPI contusion time course supports persistence plus phenotype change.", "tracker_id": "M1B-L034"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O027'
WHERE c.tracker_id = 'M1B-C013';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Transplanted SAs self-maintain N-cadherin-rich scar-like clusters, supporting robustness of scar-forming state.", "tracker_id": "M1B-L035"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O030'
WHERE c.tracker_id = 'M1B-C013';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Reseeding off collagen does not revert Col-I-SAs.", "tracker_id": "M1B-L036"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O028'
WHERE c.tracker_id = 'M1B-C014';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "In vitro beta1-integrin/N-cadherin blockade does not revert established Col-I-SAs.", "tracker_id": "M1B-L037"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O029'
WHERE c.tracker_id = 'M1B-C014';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "In vivo beta1-integrin antibody blocks recruitment and reduces chronic GFAP/N-cadherin-positive astrocytes.", "tracker_id": "M1B-L038"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O031'
WHERE c.tracker_id = 'M1B-C014';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Anti-beta1-integrin treatment reduces chronic scar-forming astrocytes and increases GAP43-positive area.", "tracker_id": "M1B-L039"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O031'
WHERE c.tracker_id = 'M1B-C015';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "IAM transcriptional time course establishes injury-activated myeloid program.", "tracker_id": "M1B-L040"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O032'
WHERE c.tracker_id = 'M1B-C016';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Plexin-B2 perturbation observation supports corralling, compaction, and border-containment claim.", "tracker_id": "M1B-L041"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O033'
WHERE c.tracker_id = 'M1B-C016';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Ryk source-page observation supports astrocyte border and wound-healing coordination claim.", "tracker_id": "M1B-L042"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O034'
WHERE c.tracker_id = 'M1B-C017';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Lineage source-page observation supports local astrocyte-majority and OPC-minority origin claim.", "tracker_id": "M1B-L043"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O035'
WHERE c.tracker_id = 'M1B-C018';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "snRNA-seq/temporal transcriptomic observation supports wound-repair astrocyte state claim.", "tracker_id": "M1B-L044"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O036'
WHERE c.tracker_id = 'M1B-C018';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'concordant_boundary',
  '{"notes": "Tamaru''s chronic phenotype-shift data is consistent with border astrocytes being dynamic rather than static scar cells.", "tracker_id": "M1B-L045"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O027'
WHERE c.tracker_id = 'M1B-C018';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "ST atlas provides tissue-wide scar region mapping over time.", "tracker_id": "M1B-L046"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O037'
WHERE c.tracker_id = 'M1B-C019';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Reclustered ST spots identify multicellular scar-resident composition and spatial ordering.", "tracker_id": "M1B-L047"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O038'
WHERE c.tracker_id = 'M1B-C019';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "ECM/ST marker maps support fibrotic core and glial boundary structure.", "tracker_id": "M1B-L048"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O039'
WHERE c.tracker_id = 'M1B-C019';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Four-phase model observation directly supports staged scar-formation claim.", "tracker_id": "M1B-L049"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O040'
WHERE c.tracker_id = 'M1B-C020';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Persistent FnEDA/FnEDB expression establishes fibronectin isoform response after SCI.", "tracker_id": "M1B-L050"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O041'
WHERE c.tracker_id = 'M1B-C021';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "FnEDA-null chronic histology supports reduced fibrotic core with preserved GFAP glial scarring.", "tracker_id": "M1B-L051"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O042'
WHERE c.tracker_id = 'M1B-C021';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Matrix fractionation supports FnEDA role in insoluble assembled fibronectin stability.", "tracker_id": "M1B-L052"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O043'
WHERE c.tracker_id = 'M1B-C021';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "FnEDA-null axon-density and behavioral results support recovery implication.", "tracker_id": "M1B-L053"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O044'
WHERE c.tracker_id = 'M1B-C022';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Smaller chronic fibrotic lesion core provides anatomical context for recovery effect.", "tracker_id": "M1B-L054"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O042'
WHERE c.tracker_id = 'M1B-C022';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Abstract-level chronic rat zone architecture and repair modification support historical claim.", "tracker_id": "M1B-L055"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O045'
WHERE c.tracker_id = 'M1B-C023';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Source-page scRNA-seq and interaction inference support multicellular ecosystem claim.", "tracker_id": "M1B-L056"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O046'
WHERE c.tracker_id = 'M1B-C024';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'concordant_boundary',
  '{"notes": "Gong spatial atlas is consistent with Milich source-page single-cell heterogeneity.", "tracker_id": "M1B-L057"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O038'
WHERE c.tracker_id = 'M1B-C024';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Lesion-remote astrocyte transcriptomic states support remote white matter as active compartment.", "tracker_id": "M1B-L058"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O047'
WHERE c.tracker_id = 'M1B-C025';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "WM3/4 LRA-WDM niche supports astrocyte-microglia repair organization.", "tracker_id": "M1B-L059"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O048'
WHERE c.tracker_id = 'M1B-C025';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Ccn1 deletion debris/recovery phenotype links remote white matter repair to outcome.", "tracker_id": "M1B-L060"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O050'
WHERE c.tracker_id = 'M1B-C025';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Ccn1-positive LRAs regulate WDM localization and magnitude.", "tracker_id": "M1B-L061"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O049'
WHERE c.tracker_id = 'M1B-C026';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Debris accumulation after Ccn1 deletion supports impaired processing mechanism.", "tracker_id": "M1B-L062"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O050'
WHERE c.tracker_id = 'M1B-C026';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "CCN1 microglia lipid assays support lipid-buffering mechanism.", "tracker_id": "M1B-L063"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O051'
WHERE c.tracker_id = 'M1B-C026';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Myelin-damage and human tissue comparisons support conservation of the CCN1-positive white matter astrocyte response.", "tracker_id": "M1B-L064"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O052'
WHERE c.tracker_id = 'M1B-C026';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Scholtes MRI/histology/BBB observation supports spared white matter imaging claim.", "tracker_id": "M1B-L065"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O053'
WHERE c.tracker_id = 'M1B-C027';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Song source-page MRI observation supports tract pathology and recovery-link claim.", "tracker_id": "M1B-L066"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O054'
WHERE c.tracker_id = 'M1B-C028';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Rosenberg abstract-level residual white matter observation supports chronic cellular remodeling claim.", "tracker_id": "M1B-L067"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O055'
WHERE c.tracker_id = 'M1B-C029';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Contusion scar resection worsened BBB recovery and failed to restore axon crossing.", "tracker_id": "M1B-L068"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O056'
WHERE c.tracker_id = 'M1B-C030';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Hemisection scar resection was neutral and failed to restore axon crossing.", "tracker_id": "M1B-L069"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O057'
WHERE c.tracker_id = 'M1B-C030';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Wang abstract-level scaffold/cell implantation observation supports chronic resection cavity repair claim.", "tracker_id": "M1B-L070"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O058'
WHERE c.tracker_id = 'M1B-C031';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Human SSEP/MEP-guided resection and BMMC-loaded scaffold implantation supports feasibility.", "tracker_id": "M1B-L071"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O059'
WHERE c.tracker_id = 'M1B-C032';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "One-year safety follow-up and SSEP recovery observations support small-cohort feasibility/safety claim.", "tracker_id": "M1B-L072"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O061'
WHERE c.tracker_id = 'M1B-C032';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Human scar-marker panel supports scar-rich/neural-marker-poor specimen claim.", "tracker_id": "M1B-L073"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O060'
WHERE c.tracker_id = 'M1B-C033';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Electrophysiology-guided mapping supports careful scar targeting but does not alone prove tissue composition.", "tracker_id": "M1B-L074"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O059'
WHERE c.tracker_id = 'M1B-C033';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Ito source-page observation supports dECM scaffold and hNS/PC histological repair strategy.", "tracker_id": "M1B-L075"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O062'
WHERE c.tracker_id = 'M1B-C034';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'concordant_boundary',
  '{"notes": "Wang abstract-level NeuroRegen+hUC-MSC strategy is directionally consistent with scaffold/cell filling after chronic resection.", "tracker_id": "M1B-L076"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O058'
WHERE c.tracker_id = 'M1B-C034';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Lesion geometry time course supports early demarcation and chronic stability claim.", "tracker_id": "M1B-L077"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O063'
WHERE c.tracker_id = 'M1B-C035';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Remote motor-system MRI changes support ongoing degeneration component.", "tracker_id": "M1B-L078"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O064'
WHERE c.tracker_id = 'M1B-C035';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Tissue bridge and remote MRI associations support clinical relevance.", "tracker_id": "M1B-L079"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O065'
WHERE c.tracker_id = 'M1B-C036';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Ventral-root large-diameter axon reduction supports motoneuron loss claim.", "tracker_id": "M1B-L080"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O066'
WHERE c.tracker_id = 'M1B-C037';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "g-ratio and thin-myelin findings support incomplete remyelination claim.", "tracker_id": "M1B-L081"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O067'
WHERE c.tracker_id = 'M1B-C038';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Pediatric DTI abnormalities in MRI-normal-appearing cord support normal-MRI limitation claim.", "tracker_id": "M1B-L082"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O068'
WHERE c.tracker_id = 'M1B-C039';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "AIS A/B versus C/D comparison supports severity-related FA abnormality claim.", "tracker_id": "M1B-L083"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O069'
WHERE c.tracker_id = 'M1B-C039';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Human scar marker profile supports persistent scar-rich component claim.", "tracker_id": "M1B-L084"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O070'
WHERE c.tracker_id = 'M1B-C040';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'concordant_boundary',
  '{"notes": "Same specimen evidence also supports T005 scar-targeting interpretation.", "tracker_id": "M1B-L085"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O060'
WHERE c.tracker_id = 'M1B-C040';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Pre-injury PLX flow cytometry/ROS/qPCR supports acute inflammation reduction.", "tracker_id": "M1B-L086"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O071'
WHERE c.tracker_id = 'M1B-C041';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Post-injury PLX 7 DPI flow cytometry supports reduced spinal and brain myeloid populations.", "tracker_id": "M1B-L087"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O072'
WHERE c.tracker_id = 'M1B-C041';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Fine motor, cognitive, and depressive-like behavior outcomes support functional component.", "tracker_id": "M1B-L088"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O073'
WHERE c.tracker_id = 'M1B-C042';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Remote neuronal survival with unchanged lesion volume supports brain pathology component.", "tracker_id": "M1B-L089"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O074'
WHERE c.tracker_id = 'M1B-C042';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Spinal NanoString/qPCR supports chronic inflammatory, apoptotic, astrocyte, and matrix program modification.", "tracker_id": "M1B-L090"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O075'
WHERE c.tracker_id = 'M1B-C042';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Cortical transcriptome and qPCR support remote brain inflammatory component.", "tracker_id": "M1B-L091"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O076'
WHERE c.tracker_id = 'M1B-C042';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Pre-injury depletion benefit in acute inflammation supports modulation but not the protective early-microglia side alone.", "tracker_id": "M1B-L092"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O071'
WHERE c.tracker_id = 'M1B-C043';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'concordant_boundary',
  '{"notes": "Zhou source-page corralling evidence supports protective/containment functions for myeloid cells.", "tracker_id": "M1B-L093"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O077'
WHERE c.tracker_id = 'M1B-C043';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Plexin-B2 source-page observation supports corralling and containment mechanism.", "tracker_id": "M1B-L094"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O077'
WHERE c.tracker_id = 'M1B-C044';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Milich source-page single-cell interaction observation supports multicellular ecosystem claim.", "tracker_id": "M1B-L095"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O078'
WHERE c.tracker_id = 'M1B-C045';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'concordant_boundary',
  '{"notes": "Same source-page evidence also supports T001 core lesion ecology.", "tracker_id": "M1B-L096"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O046'
WHERE c.tracker_id = 'M1B-C045';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Gerber source-page CSF1R inhibition observation supports tissue-preservation and recovery claim.", "tracker_id": "M1B-L097"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O079'
WHERE c.tracker_id = 'M1B-C046';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'concordant_boundary',
  '{"notes": "Li shows CSF1R inhibition effects without lesion-volume/spared-white-matter improvement, marking treatment/model boundary.", "tracker_id": "M1B-L098"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O074'
WHERE c.tracker_id = 'M1B-C046';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Focal cystic atrophy measurement supports short local lesion-zone claim.", "tracker_id": "M1B-L099"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O080'
WHERE c.tracker_id = 'M1B-C047';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Preserved rostral/caudal cord area and 2/12 syrinx cases support adjacent mass preservation boundary.", "tracker_id": "M1B-L100"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O081'
WHERE c.tracker_id = 'M1B-C047';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Short cystic lesion zone supports bridging implication but does not test repair.", "tracker_id": "M1B-L101"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O080'
WHERE c.tracker_id = 'M1B-C048';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Long remaining adjacent parenchyma supports growth-through-parenchyma implication.", "tracker_id": "M1B-L102"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O081'
WHERE c.tracker_id = 'M1B-C048';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Normal human vascular territory mapping supports sulcal arterial mechanism context.", "tracker_id": "M1B-L103"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O082'
WHERE c.tracker_id = 'M1B-C049';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Acute human pathology supports gray hemorrhagic necrosis, white matter degeneration, venous occlusion, and major-artery patency claim.", "tracker_id": "M1B-L104"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O083'
WHERE c.tracker_id = 'M1B-C049';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Chronic cavitation is the later pathology consistent with central myelomalacia.", "tracker_id": "M1B-L105"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O084'
WHERE c.tracker_id = 'M1B-C049';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'directly_supports',
  '{"notes": "Chronic rostral/caudal posterior-column infarct-like lesions support remote pathology claim.", "tracker_id": "M1B-L106"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O084'
WHERE c.tracker_id = 'M1B-C050';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'partially_supports',
  '{"notes": "Acute white matter lesions extending far from the injury site support continuity with later remote necrosis.", "tracker_id": "M1B-L107"}'
FROM _m1_claim_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O083'
WHERE c.tracker_id = 'M1B-C050';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Chronic SCI lesion architecture is a multicompartment structure, not a single scar. The core evidence supports separately queryable fibrotic or ECM-rich matrix, astrocytic border, immune/myeloid containment zone, spared or reactive neural tissue, altered white matter, and cystic or repaired-tissue cavities when present.',
    'M1B-T001: Core lesion architecture',
    1,
    'moderate',
    '{"boundary_or_contradiction_handling": "Compartment definitions vary by model, time point, assay resolution, and whether lesions are contusive, hemisection, cavitary, or scaffold-repaired; do not collapse all scar biology into one field.", "boundary_tracker_ids": [], "claim_tracker_ids": ["M1B-C019", "M1B-C020", "M1B-C021", "M1B-C022", "M1B-C023", "M1B-C024"], "consensus_draft_id": "M1B-S001", "observation_tracker_ids": ["M1B-O037", "M1B-O038", "M1B-O039", "M1B-O040", "M1B-O041", "M1B-O042", "M1B-O043", "M1B-O044", "M1B-O045", "M1B-O046"], "source_agreement_label": "moderate", "source_tracker": "modules/Module_1B_TRACKER.md", "supporting_evidence_scope": "Supported by spatial transcriptomics and scar-matrix full-text evidence, with lower-confidence abstract/source-page support for chronic zone architecture and single-cell lesion ecology; observations M1B-O037-M1B-O046; claims M1B-C019-M1B-C024.", "topic_id": "M1B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m1_consensus_map (tracker_id, consensus_id) SELECT 'M1B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O037'
WHERE c.tracker_id = 'M1B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O038'
WHERE c.tracker_id = 'M1B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O039'
WHERE c.tracker_id = 'M1B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O040'
WHERE c.tracker_id = 'M1B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O041'
WHERE c.tracker_id = 'M1B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O042'
WHERE c.tracker_id = 'M1B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O043'
WHERE c.tracker_id = 'M1B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O044'
WHERE c.tracker_id = 'M1B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O045'
WHERE c.tracker_id = 'M1B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O046'
WHERE c.tracker_id = 'M1B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'SCI fibrotic scarring arises from perivascular and meningeal-associated stromal lineages, but lineage assignment depends on marker system, Cre driver, injury geometry, dural disruption, and endpoint. The consensus is modulation, not ablation: partial attenuation can support repair in some models, whereas loss of closure-producing stroma can be harmful.',
    'M1B-T002: Fibrotic scar cellular origins',
    1,
    'moderate',
    '{"boundary_or_contradiction_handling": "M1B-X002 resolves apparent pericyte-versus-fibroblast conflicts as marker/system dependent; store marker, lineage driver, injury model, and dural status with each claim.", "boundary_tracker_ids": ["M1B-X002"], "claim_tracker_ids": ["M1B-C006", "M1B-C007", "M1B-C008", "M1B-C009", "M1B-C010", "M1B-C011", "M1B-C012"], "consensus_draft_id": "M1B-S002", "observation_tracker_ids": ["M1B-O012", "M1B-O013", "M1B-O014", "M1B-O015", "M1B-O016", "M1B-O017", "M1B-O018", "M1B-O019", "M1B-O020", "M1B-O021", "M1B-O022", "M1B-O023", "M1B-O024", "M1B-O025", "M1B-O026"], "source_agreement_label": "moderate", "source_tracker": "modules/Module_1B_TRACKER.md", "supporting_evidence_scope": "Supported by three full-text lineage/function studies; observations M1B-O012-M1B-O026; claims M1B-C006-M1B-C012.", "topic_id": "M1B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m1_consensus_map (tracker_id, consensus_id) SELECT 'M1B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O012'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O013'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O014'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O015'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O016'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O017'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O018'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O019'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O020'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O021'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O022'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O023'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O024'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O025'
WHERE c.tracker_id = 'M1B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O026'
WHERE c.tracker_id = 'M1B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Astrocytic scar borders are active wound-repair and containment structures with separable programs for formation, maintenance, recruitment, and morphology. Established scar-forming astrocytes may resist direct reversal, while border recruitment and organization remain intervention-sensitive in vivo.',
    'M1B-T003: Astrocytic border and wound-repair state',
    1,
    'moderate',
    '{"boundary_or_contradiction_handling": "M1B-X003 distinguishes established astrocyte-state reversal from border recruitment/organization. Source-page studies should remain medium confidence until full-text upgrades.", "boundary_tracker_ids": ["M1B-X003"], "claim_tracker_ids": ["M1B-C013", "M1B-C014", "M1B-C015", "M1B-C016", "M1B-C017", "M1B-C018"], "consensus_draft_id": "M1B-S003", "observation_tracker_ids": ["M1B-O027", "M1B-O028", "M1B-O029", "M1B-O030", "M1B-O031", "M1B-O032", "M1B-O033", "M1B-O034", "M1B-O035", "M1B-O036"], "source_agreement_label": "moderate", "source_tracker": "modules/Module_1B_TRACKER.md", "supporting_evidence_scope": "Strongest support comes from Tamaru 2023 full text, with source-page support from immune-corralling, Ryk, and wound-repair astrocyte studies; observations M1B-O027-M1B-O036; claims M1B-C013-M1B-C018.", "topic_id": "M1B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m1_consensus_map (tracker_id, consensus_id) SELECT 'M1B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O027'
WHERE c.tracker_id = 'M1B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O028'
WHERE c.tracker_id = 'M1B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O029'
WHERE c.tracker_id = 'M1B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O030'
WHERE c.tracker_id = 'M1B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O031'
WHERE c.tracker_id = 'M1B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O032'
WHERE c.tracker_id = 'M1B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O033'
WHERE c.tracker_id = 'M1B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O034'
WHERE c.tracker_id = 'M1B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O035'
WHERE c.tracker_id = 'M1B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O036'
WHERE c.tracker_id = 'M1B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Chronic SCI changes lesion mechanics, but stiffness direction is model- and method-dependent. No universal chronic-scar stiffness claim should be encoded without species, injury model, time point, tissue preparation, AFM method, and lesion subregion.',
    'M1B-T004: Chronic lesion biomechanics',
    1,
    'emerging',
    '{"boundary_or_contradiction_handling": "M1B-X001 is the central synthesis: rat hemisection scar softening and mouse contusion lesion stiffening are both admissible under different model/method conditions.", "boundary_tracker_ids": ["M1B-X001"], "claim_tracker_ids": ["M1B-C001", "M1B-C002", "M1B-C003", "M1B-C004", "M1B-C005"], "consensus_draft_id": "M1B-S004", "observation_tracker_ids": ["M1B-O001", "M1B-O002", "M1B-O003", "M1B-O004", "M1B-O005", "M1B-O006", "M1B-O007", "M1B-O008", "M1B-O009", "M1B-O010", "M1B-O011"], "source_agreement_label": "emerging / boundary-specific", "source_tracker": "modules/Module_1B_TRACKER.md", "supporting_evidence_scope": "Supported by two full-text mechanics studies with directly conflicting directionality; observations M1B-O001-M1B-O011; claims M1B-C001-M1B-C005.", "topic_id": "M1B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m1_consensus_map (tracker_id, consensus_id) SELECT 'M1B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O001'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O002'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O003'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O004'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O005'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O006'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O007'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O008'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O009'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O010'
WHERE c.tracker_id = 'M1B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O011'
WHERE c.tracker_id = 'M1B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Chronic scar resection divides into distinct intervention classes: tissue removal alone and resection followed by cavity or gap reconstruction. Resection alone is not consensus-reparative and may be harmful in contusion models, whereas scaffold or cell filling is a recurring but model- and endpoint-dependent reconstruction strategy.',
    'M1B-T005: Cavitary lesions, scar resection, and scaffold filling',
    1,
    'moderate',
    '{"boundary_or_contradiction_handling": "M1B-X004 resolves the apparent conflict by distinguishing tissue removal from reconstruction after resection; efficacy claims should not be generalized beyond feasibility/safety or specific animal endpoints.", "boundary_tracker_ids": ["M1B-X004"], "claim_tracker_ids": ["M1B-C030", "M1B-C031", "M1B-C032", "M1B-C033", "M1B-C034"], "consensus_draft_id": "M1B-S005", "observation_tracker_ids": ["M1B-O056", "M1B-O057", "M1B-O058", "M1B-O059", "M1B-O060", "M1B-O061", "M1B-O062"], "source_agreement_label": "moderate", "source_tracker": "modules/Module_1B_TRACKER.md", "supporting_evidence_scope": "Supported by two full-text resection/human scaffold studies plus abstract/source-page scaffold support; observations M1B-O056-M1B-O062; claims M1B-C030-M1B-C034.", "topic_id": "M1B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m1_consensus_map (tracker_id, consensus_id) SELECT 'M1B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O056'
WHERE c.tracker_id = 'M1B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O057'
WHERE c.tracker_id = 'M1B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O058'
WHERE c.tracker_id = 'M1B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O059'
WHERE c.tracker_id = 'M1B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O060'
WHERE c.tracker_id = 'M1B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O061'
WHERE c.tracker_id = 'M1B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O062'
WHERE c.tracker_id = 'M1B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Spared and lesion-remote white matter is an active recovery-linked compartment rather than normal residual tissue. It can carry chronic degeneration, repair-associated glial and immune remodeling, MRI-visible tract changes, debris and lipid-handling programs, and behavioral associations.',
    'M1B-T006: Spared and remote white matter',
    1,
    'moderate',
    '{"boundary_or_contradiction_handling": "Boundary conditions include tract, distance from lesion, injury severity, post-mortem versus in vivo imaging, and exact MRI/histology metric. Lower-access white matter papers should not carry high-confidence numeric claims yet.", "boundary_tracker_ids": [], "claim_tracker_ids": ["M1B-C025", "M1B-C026", "M1B-C027", "M1B-C028", "M1B-C029"], "consensus_draft_id": "M1B-S006", "observation_tracker_ids": ["M1B-O047", "M1B-O048", "M1B-O049", "M1B-O050", "M1B-O051", "M1B-O052", "M1B-O053", "M1B-O054", "M1B-O055"], "source_agreement_label": "moderate", "source_tracker": "modules/Module_1B_TRACKER.md", "supporting_evidence_scope": "Strongest support comes from McCallum 2026 full text, with imaging and abstract support from Scholtes, Song, and Rosenberg; observations M1B-O047-M1B-O055; claims M1B-C025-M1B-C029.", "topic_id": "M1B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m1_consensus_map (tracker_id, consensus_id) SELECT 'M1B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O047'
WHERE c.tracker_id = 'M1B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O048'
WHERE c.tracker_id = 'M1B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O049'
WHERE c.tracker_id = 'M1B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O050'
WHERE c.tracker_id = 'M1B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O051'
WHERE c.tracker_id = 'M1B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O052'
WHERE c.tracker_id = 'M1B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O053'
WHERE c.tracker_id = 'M1B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O054'
WHERE c.tracker_id = 'M1B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O055'
WHERE c.tracker_id = 'M1B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Human chronic SCI lesion architecture is multi-scale and should retain separate fields for local lesion geometry and tissue bridges, focal cystic atrophy, retained adjacent parenchyma, vascular territory and remote infarct-like pathology, scar-marker composition, segmental motoneuron/root pathology, remyelination status, perilesional DTI abnormalities, and remote motor-system degeneration.',
    'M1B-T007: Human chronic pathology and imaging geometry',
    1,
    'strong',
    '{"boundary_or_contradiction_handling": "M1B-X005 and M1B-X007 separate local lesion stability/adjacent mass preservation from remote degeneration, vascular infarct-like lesions, and syrinx-associated atrophy.", "boundary_tracker_ids": ["M1B-X005", "M1B-X007"], "claim_tracker_ids": ["M1B-C035", "M1B-C036", "M1B-C037", "M1B-C038", "M1B-C039", "M1B-C040", "M1B-C047", "M1B-C048", "M1B-C049", "M1B-C050"], "consensus_draft_id": "M1B-S007", "observation_tracker_ids": ["M1B-O063", "M1B-O064", "M1B-O065", "M1B-O066", "M1B-O067", "M1B-O068", "M1B-O069", "M1B-O070", "M1B-O080", "M1B-O081", "M1B-O082", "M1B-O083", "M1B-O084"], "source_agreement_label": "strong first-pass", "source_tracker": "modules/Module_1B_TRACKER.md", "supporting_evidence_scope": "Supported by five full-text human studies plus source-page pediatric DTI support; observations M1B-O063-M1B-O070 and M1B-O080-M1B-O084; claims M1B-C035-M1B-C040 and M1B-C047-M1B-C050.", "topic_id": "M1B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m1_consensus_map (tracker_id, consensus_id) SELECT 'M1B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O063'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O064'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O065'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O066'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O067'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O068'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O069'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O070'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O080'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O081'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O082'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O083'
WHERE c.tracker_id = 'M1B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O084'
WHERE c.tracker_id = 'M1B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Immune-glial lesion biology is phase-, cell-, function-, and endpoint-specific. Myeloid and glial responses can support corralling, compaction, containment, debris handling, and repair while also contributing to chronic neuroinflammatory pathology and remote effects.',
    'M1B-T008: Immune-glial containment and chronic inflammation',
    1,
    'moderate',
    '{"boundary_or_contradiction_handling": "M1B-X006 resolves the main tension as phase- and function-specific: protective early containment/debris roles can coexist with chronic inflammatory harm. Source-page mechanistic rows remain medium confidence.", "boundary_tracker_ids": ["M1B-X006"], "claim_tracker_ids": ["M1B-C041", "M1B-C042", "M1B-C043", "M1B-C044", "M1B-C045", "M1B-C046"], "consensus_draft_id": "M1B-S008", "observation_tracker_ids": ["M1B-O071", "M1B-O072", "M1B-O073", "M1B-O074", "M1B-O075", "M1B-O076", "M1B-O077", "M1B-O078", "M1B-O079"], "source_agreement_label": "moderate", "source_tracker": "modules/Module_1B_TRACKER.md", "supporting_evidence_scope": "Supported by Li 2020 full text plus source-page evidence from Zhou, Milich, and Gerber; observations M1B-O071-M1B-O079; claims M1B-C041-M1B-C046.", "topic_id": "M1B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m1_consensus_map (tracker_id, consensus_id) SELECT 'M1B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O071'
WHERE c.tracker_id = 'M1B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O072'
WHERE c.tracker_id = 'M1B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O073'
WHERE c.tracker_id = 'M1B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O074'
WHERE c.tracker_id = 'M1B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O075'
WHERE c.tracker_id = 'M1B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O076'
WHERE c.tracker_id = 'M1B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O077'
WHERE c.tracker_id = 'M1B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O078'
WHERE c.tracker_id = 'M1B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m1_consensus_map c
JOIN _m1_observation_map o ON o.tracker_id = 'M1B-O079'
WHERE c.tracker_id = 'M1B-S008';

DO $$
DECLARE
  paper_count INTEGER;
  experiment_count INTEGER;
  observation_count INTEGER;
  claim_count INTEGER;
  link_count INTEGER;
  consensus_count INTEGER;
  consensus_observation_count INTEGER;
BEGIN
  SELECT COUNT(*) INTO paper_count FROM _m1_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m1_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m1_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m1_claim_map;
  SELECT COUNT(*) INTO link_count FROM EvidenceLink;
  SELECT COUNT(*) INTO consensus_count FROM _m1_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count FROM Consensus_Observation;
  IF paper_count <> 28 THEN RAISE EXCEPTION 'Expected 28 papers, found %', paper_count; END IF;
  IF experiment_count <> 87 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 84 THEN RAISE EXCEPTION 'Expected 84 observations, found %', observation_count; END IF;
  IF claim_count <> 50 THEN RAISE EXCEPTION 'Expected 50 claims, found %', claim_count; END IF;
  IF link_count <> 107 THEN RAISE EXCEPTION 'Expected 107 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 84 THEN RAISE EXCEPTION 'Expected 84 consensus-observation links, found %', consensus_observation_count; END IF;
END $$;

COMMIT;
