import sys
import os.path, shutil
import traceback

outfile = sys.argv[1]

years=list(range(1990,2099))

min_year = 0
pub_num = 0

def get_year(cite):
    for y in years:
        if str(y) in cite:
            return y
    assert 0, cite

all_papers = []
class Paper(object):
    def __init__(self, **kw):
        if not 'title' in kw:
            assert 0
        if not 'author' in kw:
            assert 0
        if not 'citation' in kw:
            print 'no citation info for %s' % (kw['title'],)
        if not 'pdf' in kw:
            print 'no pdf info for %s' % (kw['title'],)
        else:
            if not os.path.exists(kw['pdf']):
                print 'no PDF file for %s' % (kw['title'],)
        if 'contribution' not in kw:
            print 'no contribution stmt for %s' % (kw['title'],)

        global min_year
        x = get_year(kw['citation'])
        if x > min_year:
            min_year = x
        if x < min_year:
            assert 0, kw['title']

        global pub_num
        pub_num += 1
        self.pub_num = pub_num

        self.info = kw

        sys.stdout.write('.')
        sys.stdout.flush()

        all_papers.append(self)

    def copypdf(self):
        kw = self.info
        self.pdf_name = ''
        if 'pdf' in kw:
            pdf_name = 'output/paper%03d-%s' % (self.pub_num, kw['pdf'])
            try:
                shutil.copy(kw['pdf'], pdf_name)
            except IOError:
                traceback.print_exc()
            self.pdf_name = pdf_name

    def output(self, fp):
        def title(info):
            t = info['title']
            t.rstrip('.')
            return '<i>%s.</i>' % (t,)
        
        def authors(info):
            a = info['author']
            if "et al." in a:
                return a

            a = a.rstrip('.')
            x = a.split(',')
            x = [ i.strip() for i in x ]
            if len(x) == 1:
                return x[0] + '.'
            a = ", ".join(x[:-1])
            a += ' and ' + x[-1]

            if "C. Titus Brown" in a:
                a = a.replace('C. Titus Brown', '<b>C. Titus Brown</b>')
            
            return a + '.'
        
        note = ''
        if 'note' in self.info:
            note = "* Note: %s<br>" % self.info['note']

        print >>fp, '%d. %s<br>' % (self.pub_num, title(self.info))
        print >>fp, '<blockquote>'
        print >>fp, '%s<br>' % (authors(self.info),)
        print >>fp, '%s<br>' % (self.info['citation'])
        print >>fp, note
        print >>fp, '<p>'
        print >>fp, 'Contribution: %s' % (self.info['contribution'])
        print >>fp, '<p>'
        if self.pdf_name:
            print >>fp, "<A href='%s'>[ view pdf: %s ]</a>" % (self.pdf_name, self.pdf_name.split('/')[1])
        print >>fp, '</blockquote>'
        print >>fp, '<p>'

Paper(title="Evolutionary learning in the 2D Artificial Life System \"Avida\"",
      tags="avida",
      pdf="1994-avida.pdf",
      link="http://books.google.com/books?id=8a6uC0BbyjAC&pg=PA377#v=onepage&q&f=false",
      author="Christoph Adami,C. Titus Brown",
      citation="Proc. of Artificial Life IV, MIT Press, p. 377-381 (1994)",
      contribution="I implemented the majority of the Avida computational research system, conducted all the computational experiments, and co-wrote the paper.")

Paper(title="Abundance-distributions in artificial life and stochastic models: \"age and area\" revisited",
      tags="avida,alife,dry",
      author="Christoph Adami,C. Titus Brown,Michael R. Haggerty",
      citation="Proc. of 3rd Europ. Conf. on Artificial Life, June 4-6, 1995, Granada, Spain, Lecture Notes in Computer Science, Springer Verlag (1995), p.503.",
      pdf='1995-avida.pdf',
      contribution="I implemented new software features required for the study, conducted those computational experiments, and co-wrote the paper.")

Paper(title="A comparison of evolutionary activity in artificial evolving systems and in the biosphere",
      tags="avida,alife,dry",
      author="Mark A. Bedau, Emile Snyder, C. Titus Brown, Norman H. Packard",
      citation="Proceedings of the 4th Europ. Conf. on Artificial Life, July, 1997",
      pdf='1997-bedau.pdf',
      contribution="I implemented new software features required for the study, conducted computational experiments, interpreted results, and co-wrote the paper.")

Paper(title="Visualizing evolutionary activity of genotypes",
      tags="avida,alife,dry",
      citation="Artif Life. 1999 Winter;5(1):17-35.",
      author="Mark A. Bedau,C. Titus Brown",
      pdf='1999-bedau.pdf',
      contribution="I implemented new software features required for the study, conducted computational experiments, interpreted results, and co-wrote the paper.")

Paper(title="Earthshine Observations of the Earth's Reflectance",
      tags="earthshine,observing",
      author="Phil R. Goode, J. Qiu, V. Yurchyshyn, J. Hickey, M-C. Chu, E. Kolbe, C. Titus Brown, Steven E. Koonin",
      citation="Geophysical Research Letters Volume 28, Issue 9, pages 1671-1674, 1 May 2001",
      doi="10.1029/2000GL012580",
      pdf='2001-goode.pdf',
      contribution="I wrote the analysis platform, conducted experiments, and interpreted results.")

Paper(title="SUNSHINE, EARTHSHINE AND CLIMATE CHANGE: II. SOLAR ORIGINS OF VARIATIONS IN THE EARTH'S ALBEDO",
      tags="earthshine,observing",
      author="P. R. Goode, E. Palle, V. Yurchyshyn, J. Qiu, J. Hickey, P. Montanes Rodriguez, M.-C. Chu, E. Kolbe, C. Titus Brown, Steven E. Koonin",
      citation="Journal of The Korean Astronomical Society, 35: 1-7, 2002",
      contribution="Collected observational data; rewrote and implemented computational analysis pipeline",
      pdf="2002-sunshine.pdf")
      
Paper(title="A provisional regulatory gene network for specification of endomesoderm in the sea urchin embryo",
      tags="sea urchin,gene regulatory network",
      author="Eric H. Davidson et al.",
      citation="Dev Biol. 2002 Jun 1;246(1):162-90",
      contribution="Co-designed, implemented, and executed bioinformatics analysis",
      pdf="2002-grn-devbio.pdf")

Paper(title="A genomic regulatory network for development",
      tags="sea urchin,gene regulatory network",
      author="Eric H. Davidson et al.",
      citation="Science. 2002 Mar 1;295(5560):1669-78",
      doi="10.1126/science.1069883",
      contribution="Co-designed, implemented, and executed bioinformatics analysis",
      pdf="2002-grn-science.pdf")

Paper(title="New computational approaches for analysis of cis-regulatory networks",
      tags="sea urchin,bioinformatics",
      author="C. Titus Brown, Alistair G. Rust, Peter J. Clarke, Z. Pan, M. J. Schilstra, T. De Buysscher, G. Griffin, Barbara J. Wold, R. Andrew Cameron, Eric H. Davidson, Hamid Bolouri",
      citation="Dev Biol. 2002 Jun 1;246(1):86-102",
      contribution="Implemented part of the software; wrote the paper",
      pdf="2002-cisreg.pdf")

Paper(title="Patchy interspecific sequence similarities efficiently identify positive cis-regulatory elements in the sea urchin",
      tags="sea urchin,bioinformatics",
      author="C. H. Yuh, C. Titus Brown, Carolina B. Livi, L. Rowen, Peter J. Clarke, Eric H. Davidson",
      citation="Dev Biol. 2002 Jun 1;246(1):148-61",
      contribution="Designed and implemented computational workflow",
      pdf="2002-patchy.pdf")

Paper(title="Earthshine and the Earth's albedo: 1. Earthshine observations and measurements of the lunar phase function for accurate measurements of the Earth's Bond albedo",
      tags="earthshine,observing",
      author="J. Qiu, P. R. Goode, E. Palle, V. Yuchyshyn, J. Hickey, P. Montanes Rodriguez, M.-C. Chu, E. Kolbe, C. Titus Brown, Steven E. Koonin",
      citation="JOURNAL OF GEOPHYSICAL RESEARCH, VOL. 108, NO. D22, 4709 (2003)",
      doi="10.1029/2003JD003610",
      contribution="Collected observational data; rewrote and implemented computational analysis pipeline",
      pdf="2003-earthshine-qiu.pdf")

Paper(title="Earthshine and the Earth's albedo: 2. Observations and simulations over 3 years",
      tags="earthshine,observing",
      citation="JOURNAL OF GEOPHYSICAL RESEARCH, VOL. 108, NO. D22, 4710 (2003)",
      author="E. Palle, P. R. Goode, V. Yurchyshyn, J. Qiu, J. Hickey, P. Montanes Rodriguez, M.-C. Chu, E. Kolbe, C. Titus Brown, Steven E. Koonin",
      doi="10.1029/2003JD003611",
      contribution="Collected observational data; rewrote and implemented computational analysis pipeline",
      pdf="2003-earthshine-2.pdf")

Paper(title="The earthshine spectrum",
      tags="earthshine,observing",
      author="P. M. Rodriguez, E. Palle, P. R. Goode, J. Hickey, J. Qiu, V. Yurchyshyn, M.-C. Chu, E. Kolbe, C. T. Brown, and S. E. Koonin",
      citation="Solar Variability and Climate Change Advances in Space Research 34, 293 (2004)",
      contribution="Collected observational data; rewrote and implemented computational analysis pipeline",
      pdf="2004-earthshine-spectrum.pdf")

Paper(title="The Earthshine Project: update on photometric and spectroscopic measurements",
      tags="earthshine,observing",
      author="E. Palle, P. Montanes Rodriguez, P. R. Goode, J. Qiu, V.  Yurchyshyn, J. Hickey, M.-C. Chu, E. Kolbe, C. Titus Brown, Steven E. Koonin",
      pdf="2004-earthshine-update.pdf",
      contribution="Collected observational data; rewrote and implemented computational analysis pipeline",
      citation="Advances in Space Research 34 (2004) 288-292")

Paper(title="Evolutionary comparisons suggest many novel cAMP response protein binding sites in Escherichia coli",
      tags="microbial,bioinformatics",
      citation="Proc Natl Acad Sci U S A. 2004 Feb 24;101(8):2404-9",
      author="C. Titus Brown, Curtis G. Callan",
      contribution="Implemented and executed computational workflow, co-wrote paper",
      pdf="2004-crp.pdf")

Paper(title="Genomic Resources for the Study of Sea Urchin Development",
      tags="chapter,invited,bioinformatics,sea urchin",
      author="R. Andrew Cameron,Jonathan P. Rast, C. Titus Brown",
      citation="Methods in Cell Biology, Volume 74, 2004, Pages 733-757",
      contribution="Co-wrote paper.",
      pdf="2004-cameron.pdf",
      note="Invited chapter; not peer-reviewed.")

Paper(title="Anaerobic regulation by an atypical Arc system in Shewanella oneidensis",
      tags="microbial,bioinformatics",
      citation="Mol Microbiol. 2005 Jun;56(5):1347-57",
      author="Jeffrey A. Gralnick, C. Titus Brown, Dianne K. Newman",
      contribution="Designed, implemented, and executed computational workflow",
      pdf="2005-jeff.pdf")

Paper(title="Paircomp, FamilyRelationsII and Cartwheel: tools for interspecific sequence comparison",
      tags="bioinformatics,genomics",
      author="C. Titus Brown, Yuan Xie, Eric H. Davidson, R. Andrew Cameron",
      citation="BMC Bioinformatics. 2005 Mar 24;6:70.",
      contribution="Developed software, wrote paper",
      pdf="2005-cartwheel.pdf")

Paper(title="Sea urchin Forkhead gene family: phylogeny and embryonic expression",
      tags="bioinformatics,genomics,sea urchin",
      citation="Dev Biol. 2006 Dec 1;300(1):49-62",
      author="Qiang Tu, C. Titus Brown, Eric H. Davidson, Paola Oliveri",
      contribution="Designed, implemented, and executed computational workflow",
      pdf='2006-tf-forkhead.pdf')

Paper(title="Identification and characterization of homeobox transcription factor genes in Strongylocentrotus purpuratus, and their expression in embryonic development",
      tags="bioinformatics,genomics,sea urchin",
      author="Meredith Howard-Ashby, Stefan C. Materna, C. Titus Brown, Lili Chen, R. Andrew Cameron, Eric H. Davidson",
      citation="Dev Biol. 2006 Dec 1;300(1):74-89",
      contribution="Designed, implemented, and executed computational workflow",
      pdf='2006-tf-homeobox.pdf')

Paper(title="Gene families encoding transcription factors expressed in early development of Strongylocentrotus purpuratus",
      tags="bioinformatics,genomics,sea urchin",
      author="Meredith Howard-Ashby, Stefan C. Materna, C. Titus Brown, Lili Chen, R. Andrew Cameron, Eric H. Davidson",
      citation="Dev Biol. 2006 Dec 1;300(1):90-107",
      contribution="Designed, implemented, and executed computational workflow",      pdf='2006-tf-expr.pdf')

Paper(title="High regulatory gene use in sea urchin embryogenesis: Implications for bilaterian development and evolution",
      author="Meredith Howard-Ashby, Stefan C. Materna, C. Titus Brown, Qiang Tu, Paola Oliveri, R. Andrew Cameron, Eric H. Davidson",
      tags="bioinformatics,genomics,sea urchin",
      citation="Dev Biol. 2006 Dec 1;300(1):27-34",
      contribution="Designed, implemented, and executed computational workflow",
      pdf="2006-tf-overview.pdf")

Paper(title="The genome of the sea urchin Strongylocentrotus purpuratus",
      author="E. Sodergren et al.",
      tags="bioinformatics,genomics,sea urchin",
      doi="10.1126/science.1133609",
      citation="Science 10 November 2006: Vol. 314 no. 5801 pp. 941-952",
      contribution="Helped annotate genome, wrote transcription factor section of paper, and supported computational work",
      pdf="2006-genome.pdf")

Paper(title='Diverse syntrophic partnerships from deep-sea methane vents revealed by direct cell capture and metagenomics',
      tags="microbial,bioinformatics,metagenomics",
      citation='Proc Natl Acad Sci U S A. 2008 May 13;105(19):7052-7',
      pdf='2008-orphan.pdf',
      contribution="Conducted computational development, workflow, and analysis; co-wrote paper",
      author="A. Pernthaler, A. E. Dekas, C. Titus Brown, Shana K. Goffredi, T. Embaye, Victoria J. Orphan")

Paper(title="Computational Approaches to Finding and Analyzing cis-Regulatory Elements",
      author="C. Titus Brown",
      tags="chapter,invited,bioinformatics",
      citation="Methods in Cell Biology, Volume 87, 2008, pages 337-365",
      contribution="Wrote chapter.",
      pdf='2008-cisreg-methods.pdf',
      note="Invited chapter; not peer reviewed.")

Paper(title='Exploring the future of bioinformatics data sharing and mining with Pygr and Worldbase',
      tags="pygr,bioinformatics",
      author="Christopher Lee, Alexander Alekseyenko, C. Titus Brown",
      citation="Proceedings of the 8th Python in Science conference (SciPy 2009), G Varoquaux, S van der Walt, J Millman (Eds.), pp. 62-67",
      contribution="Co-authored software",
      pdf='2009-pygr.pdf')

Paper(author="Jack A. Gilbert",
      tags="metagenomics,meeting report",
      title='Meeting report: the terabase metagenomics workshop and the vision of an Earth microbiome project',
      citation='Stand Genomic Sci. 2010 Dec 25;3(3):243-8',
      doi='10.4056/sigs.1433550',
      contribution="Participated in meeting and contributed to writing",
      pdf='2010-terabase.pdf')
      
Paper(title="Standing Genetic Variation in Contingency Loci Drives the Rapid Adaptation of Campylobacter jejuni to a Novel Host",
      tags="microbial,bioinformatics,genomics,campy",
      author="J. Jp. Jerome, Julia A. Bell, A. E. Plovanich-Jones, Jeffrey E. Barrick, C. Titus Brown, Linda S. Manfield",
      citation="PLoS One. 2011 Jan 24;6(1):e16399",
      doi="10.1371/journal.pone.0016399",
      contribution="Supervised computational work",
      pdf='2011-campy.pdf')

Paper(title='Metagenomics: the paths forward',
      tags="metagenomics,chapter,invited",
      author="C. Titus Brown, James M. Tiedje",
      citation='in Handbook of Molecular Microbial Ecology II: Metagenomics in Different Habitats (ed F. J. de Bruijn), John Wiley & Sons, Inc., Hoboken, NJ, USA (2011)',
      doi='10.1002/9781118010549.ch54',
      contribution="Co-wrote chapter",
      pdf='2011-metagenomics.pdf',
      note="Invited chapter; not peer reviewed.")

Paper(title="khmer: Working with Big Data in Bioinformatics",
      author="Rosangela Canino-Koening,C. Titus Brown",
      contribution="Co-wrote paper",
      citation="in Architecture of Open Source Applications, A. Brown and G. V. Wilson (ed), June 2011",
      pdf="2011-continuous-integration.pdf",
      note="Invited chapter; not peer reviewed.")

Paper(title="Changing computational research. The challenges ahead",
      tags="superior software,editorial",
      citation="Source Code Biol Med. 2012 May 28;7(1):2",
      author="Cameron Neylon et al.",
      contribution="Contributed to writing",
      doi="10.1186/1751-0473-7-2",
      pdf='2012-neylon.pdf')

Paper(title='Scaling metagenome sequence assembly with probabilistic de Bruijn graphs',
      tags='metagenomics,de bruijn graphs',
      author='Jason Pell,Arend Hintze,Rosangela Canino-Koening,Adina Howe, James M. Tiedje, C. Titus Brown',
      citation='Proc Natl Acad Sci U S A. 2012 Aug 14;109(33):13272-7',
      doi='10.1073/pnas.1121464109',
      pdf='2012-pnas-pell.pdf',
      contribution="Supervised and funded research and software development, interpreted results, co-wrote paper.")

Paper(title="Draft genome sequences of two Campylobacter jejuni clinical isolates, NW and D2600",
      author="J. P. Jerome, Brian D. Klahn, Julia A. Bell, Jeffrey E. Barrick, C. Titus Brown, Linda S. Mansfield",
      citation="J Bacteriol. 2012 Oct;194(20):5707-8.",
      contribution="Supervised computational work",
      pdf='2012-campy-genomes.pdf')

Paper(title="Cephalopod genomics: A plan of strategies and organization",
      author="Caroline B. Albertin et al.",
      citation='Stand Genomic Sci. 2012 Oct 10;7(1):175-88.',
      doi='10.4056/sigs.3136559',
      pdf='2012-cephseq.pdf',
      contribution='Wrote section on data sharing')

Paper(title="Sequencing of the sea lamprey (Petromyzon marinus) genome provides insights into vertebrate evolution",
      author="Jeramiah J. Smith et al.",
      citation="Nat Genet. 2013 Apr;45(4):415-21, 421e1-2",
      doi="10.1038/ng.2568",
      contribution="Helped annotate and quality-control computational work, helped edit paper",
      pdf='2013-lamprey-genome.pdf')

Paper(title="A thermogenic secondary sexual character in male sea lamprey",
      author="Yu-Wen Chung-Davidson, M.C. Priess, C.-Y. Yeh, C. O. Brant, N.S. Johnson, K. Li, Kaben G. Nanlohy, M.B. Bryan, C. Titus Brown, J. Choi, Weming Li",
      citation="Journal of Experimental Biology. 2013 Jul 15;216(Pt14):2702-12",
      doi="10.1242/jeb.085746",
      contribution="Helped develop and provide computational materials for study, and helped design computational workflow",
      pdf='2013-lamprey-brownfat.pdf')

Paper(title="The sea lamprey has a primordial accessory olfactory system",
      author="S. Chang, Yu-wen Chung Davidson, Scott V. Libants, Kaben G. Nanlohy, M. Kiupel, C. Titus Brown, Weiming Li",
      citation="BMC Evol Biol. 2013 Aug 17;13:172",
      contribution="Helped develop and provide computational materials for study",
      doi="10.1186/1471-2148-13-172",
      pdf='2013-lamprey-olfactory.pdf')

Paper(title="Integrated analyses of genome-wide DNA occupancy and expression profiling identify key genes and pathways involved in cellular transformation by a Marek's disease virus oncoprotein, Meq.",
      author="Suga Subramaniam, John Johnston, Likit Preeyanon, C. Titus Brown, H.J. Kung, Hans H. Cheng",
      doi="10.1128/JVI.01163-13",
      contribution="Helped design computational workflow",
      citation="J Virol. 2013 Aug;87(16):9016-29",
      pdf='2013-suga.pdf')

Paper(title="The genome and developmental transcriptome of the strongylid nematode Haemonchus contortus",
      author="Erich M. Schwarz, P. K. Korhonen, B.E. Campbell, N.D. Young, A.R. Jex, A. Jabbar, R.S. Hall, A. Mondal, A.C. Howe, J. Pell, A. Hofmann, P.R. Boag, X.Q. Zhu, T.R. Gregory, A. Loukas, B.A. Williams, I. Antoshechkin, C. Titus Brown, Paul W. Sternberg, Robin B. Gasser",
      citation="Genome Biol. 2013 Aug 28;14(8):R89",
      contribution="Helped design computational workflow and debug genome assembly problems",
      doi='10.1186/gb-2013-14-8-r89',
      pdf='2013-haemonch.pdf')

Paper(title="FunGene: the Functional Gene Pipeline and Repository",
      author="Jordan A. Fish,Benli Chai, Qiong Wang, Yanni Sun, C. Titus Brown, James M. Tiedje, James R. Cole",
      citation="Front. Microbiology. 4:291 (2013)",
      doi="10.3389/fmicb.2013.00291",
      contribution="Discussed and helped design pipeline components",
      pdf='2013-fungene.pdf')

Paper(title="khmer: Working with Big Data in Bioinformatics",
      author="Eric McDonald,C. Titus Brown",
      contribution="Co-wrote paper",
      citation="in Performance of Open Source Applications, T. Armstrong, November 2013",
      pdf="2013-khmer-posa.pdf",
      note="Invited chapter; not peer reviewed.")

Paper(title="Best Practices for Scientific Computing",
      author="Greg V. Wilson, D. A. Aruliah, C. Titus Brown, Neil P. Chue Hong, Matt Davis, Richard T. Guy, Steven H.D. Haddock, Kathryn D. Huff, Ian M. Mitchell, Mark D. Plumbley, Ben Waugh, Ethan P. White, Paul Wilson",
      citation="PLoS Biol 12(1): e1001745 (2014)",
      doi="10.1371/journal.pbio.1001745",
      contribution="Helped outline, write and edit paper",
      pdf='2014-best-practices.pdf')

Paper(title="Genomic versatility and functional variation between two dominant heterotrophic symbionts of deep-sea Osedax worms",
      author="Shana K. Goffredi, Hana Yi, Qingpeng Zhang, J.E. Klann, I.A. Struve, R.C. Vrijenhoek, C. Titus Brown",
      citation="ISME J. 2014 Apr;8(4):908-24.",
      doi="0.1038/ismej.2013.201",
      contribution="Co-supervised computational design and work, helped write paper",
      pdf='2014-osedax-paper.pdf')

Paper(title="Ribosomal Database Project: data and tools for high throughput rRNA analysis",
      author="James R. Cole, Qiong Wang, Jordan A. Fish, Benli Chai, Donna M. McGarrell, Yanni Sun, C. Titus Brown, A. Porras-Alfaro, C.R. Kuske, James M. Tiedje",
      citation="Nucleic Acids Res. 2014 Jan;42(Database issue):D633-42",
      doi="10.1093/nar/gkt1244",
      contribution="Discussed analyses and software design.",
      pdf='2014-rdp-paper.pdf')

Paper(title="Tackling soil diversity with the assembly of large, complex metagenomes",
      author="Adina Chuang Howe, Janet K. Jansson, Stephanie A. Malfatti, Susannah G. Tringe, James M. Tiedje, C. Titus Brown",
      citation="Proc Natl Acad Sciences U S A. 2014 Apr 1;111(13):4904-9.",
      doi="10.1073/pnas.1402564111",
      contribution="Supervised and funded research and software development, interpreted results, co-wrote paper.",
      pdf='2014-pnas-soil.pdf')
      
Paper(title="These are not the k-mers you are looking for: efficient online k-mer counting using a probabilistic data structure.",
      author="Qingpeng Zhang, Jason Pell, Rosangela Canino-Koning, Adina Chuang Howe, C. Titus Brown",
      citation="PLoS ONE 9(7): e101271 (2014)",
      pdf="2014-khmer-counting.pdf",
      doi="10.1371/journal.pone.0101271",
      contribution="Supervised and funded research and software development, interpreted results, co-wrote paper.")

Paper(title="Reproducible Bioinformatics Research for Biologists",
      author="Likit Preeyanon, Alexis Black Pyrkosz, C. Titus Brown",
      citation="in Implementing Reproducible Research, Stodden, Leisch and Peng. CRC Press (2014)",
      pdf="2014-repro-chapter.pdf",
      contribution="Supervised writing, co-wrote, and edited",
      note="Invited chapter; not peer reviewed.")

####

print ''
print pub_num, 'total'

print 'copying pdfs'
for p in all_papers:
    p.copypdf()

fp = open(outfile, 'w')
print >>fp, "<h2>Paper list for C. Titus Brown</h2>"
for p in all_papers:
    p.output(fp)
    
