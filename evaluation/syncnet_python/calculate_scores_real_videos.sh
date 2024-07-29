# rm all_scores.txt
# yourfilenames=`ls $1`

# for eachfile in $yourfilenames
# do
#    python run_pipeline.py --videofile $1/$eachfile --reference wav2lip --data_dir tmp_dir
#    python calculate_scores_real_videos.py --videofile $1/$eachfile --reference wav2lip --data_dir tmp_dir >> all_scores.txt
# done

rm all_scores.txt
yourfilenames=`ls $1`

counter=0
echo "=================================== List of Input Files ==================================="
for eachfile in $yourfilenames
do
  counter=$((counter + 1))
  echo "$counter.\t$eachfile"
done
echo "============================================================================================\n"

ID=0
echo "ID,FileName,LSE_D,LSE_C" > all_scores.txt
for eachfile in $yourfilenames
do
  echo "\n\n\n####################################################################################################################"
  echo "==============================================================================================================="
  echo "==================== File Under Process: $eachfile ============================================"
  echo "================================================================================================================"
  echo "#########################################################################################################################"
  ID=$((ID + 1))
  echo -n "$ID," >> all_scores.txt
  python run_pipeline.py --videofile $1$eachfile --reference wav2lip --data_dir tmp_dir
  python calculate_scores_real_videos.py --videofile $1$eachfile --reference wav2lip --data_dir tmp_dir >> all_scores.txt
done

