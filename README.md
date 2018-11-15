<h1>logs analysis project</h1>

<body>

<p>logs analysis project</p>

<h2>Operating requirements</h2>
<h3>Vagrnt</h3>
<h3>Virtual Machine</h3>
<h3>Python 3</h3>
<h3>FSND virtual machine ( From this link 	https://github.com/udacity/fullstack-nanodegree-vm )</h3>

<h2>Follow the instructions below</h2>
<pre>
	<code>

cd vagrant
vagrant up
vagrant ssh
cd /vagrant
git clone https://github.com/amjadzaghloul/Logs-Analysis.git
cd Logs-Analysis
		
</code>

</pre>

<p>Download "newsdata" from this link https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
</p>

<p>Move	the	“newsdata.sql” to project folder “Logs-Analysis”	</p>

<h2>load database</h2>
<pre><code>psql -d news -f newsdata.sql </code></pre>

<h2>run database</h2>
<pre><code>psql -d news</code></pre>

<h2>Views</h2>

<h2>three_articles</h2>
<pre><code>create view three_articles as select title, count(*) as views from articles , log  where articles.slug = substr(log.path, 10) group by title order by views DESC limit 3;</code></pre>

<h2>most_popular_article</h2>
<pre><code>create view most_popular_article as select name, count(*) as views from authors , articles , log where articles.slug = substr(log.path,10) and articles.author = authors.id group by name order by views DESC;</code></pre>

<h2>re_d</h2>
<pre><code>create view re_d as select date(time) as day, count(*) as total from log group by date(time);</code></pre>

<h2>err_d</h2>
<pre><code>create view err_d as select date(time) as day, count(*) as total from log where status != '200 OK' group by day;</code></pre>

<h2>err_r</h2>
<pre><code>create view err_r as select re_d.day, round(100.0*err_d.total/re_d.total, 2) as error_rate from err_d, re_d where err_d.day = re_d.day;</code></pre>

<h2>Run the project</h2>
<pre><code>python project.py</code></pre>

</body>
